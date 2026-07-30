import argparse
import sys
from pathlib import Path
from typing import Iterator

from batch_clubs.adapters.csv_sink import CsvClubSink
from batch_clubs.adapters.jsonl_source import JsonlClubSource
from batch_clubs.domain.club_parser import parse_club, parse_players
from batch_clubs.domain.models import Club, Player
from batch_clubs.ports.sink import ClubSink
from batch_clubs.ports.source import ClubSource


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Processa um arquivo JSONL de clubes")
    parser.add_argument("input_file", help="Caminho do arquivo JSONL de entrada")
    parser.add_argument(
        "output_dir",
        nargs="?",
        default="output",
        help="Diretório onde os arquivos CSV serão escritos (padrão: output)",
    )
    return parser


def iter_valid_clubs(source: ClubSource) -> Iterator[tuple[Club, list[dict]]]:
    for raw in source.read():
        club = parse_club(raw)
        if club is None:
            continue

        raw_players = raw.get("players") or []
        if not isinstance(raw_players, list):
            raw_players = []
        yield club, raw_players


def iter_players(club_id: str, raw_players: list[dict]) -> Iterator[Player]:
    for player in parse_players(club_id, raw_players):
        yield player


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    input_path = Path(args.input_file)
    output_dir = Path(args.output_dir)

    try:
        with input_path.open("r", encoding="utf-8") as handle:
            pass
    except FileNotFoundError:
        print(f"Erro: arquivo de entrada não encontrado: {input_path}", file=sys.stderr)
        return 1
    except OSError as exc:
        print(f"Erro ao abrir o arquivo de entrada: {exc}", file=sys.stderr)
        return 1

    output_dir.mkdir(parents=True, exist_ok=True)
    source: ClubSource = JsonlClubSource(str(input_path))
    sink: ClubSink = CsvClubSink(str(output_dir / "clubs.csv"), str(output_dir / "players.csv"))

    for club, raw_players in iter_valid_clubs(source):
        sink.write_clubs(iter([club]))
        sink.write_players(iter_players(club.club_id, raw_players))

    return 0
