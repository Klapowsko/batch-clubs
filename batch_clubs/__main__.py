import argparse
import sys
from pathlib import Path

from .club_parser import parse_club, parse_players
from .reader import read_jsonl
from .writer import write_clubs_csv, write_players_csv


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

    clubs = []
    players = []

    for raw in read_jsonl(str(input_path)):
        club = parse_club(raw)
        if club is None:
            continue

        clubs.append(club)
        raw_players = raw.get("players") or []
        if not isinstance(raw_players, list):
            raw_players = []
        players.extend(parse_players(club.club_id, raw_players))

    write_clubs_csv(str(output_dir / "clubs.csv"), clubs)
    write_players_csv(str(output_dir / "players.csv"), players)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
