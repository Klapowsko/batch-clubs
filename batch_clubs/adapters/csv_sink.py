import csv
from typing import Iterator

from batch_clubs.domain.models import Club, Player
from batch_clubs.ports.sink import ClubSink


CLUB_COLUMNS = [
    "Id do Clube",
    "Nome",
    "Campeonato",
    "Data de Fundação",
    "Cidade",
    "Estado",
    "País",
    "Estádio",
    "Presidente",
    "Apelido",
    "Cores",
]

PLAYER_COLUMNS = [
    "Id do Clube",
    "Id do Jogador",
    "Nome",
    "Idade",
    "Gols",
    "Data de Estreia",
    "Posição",
    "Número da Camisa",
]


class CsvClubSink(ClubSink):
    def __init__(self, clubs_filepath: str, players_filepath: str) -> None:
        self.clubs_filepath = clubs_filepath
        self.players_filepath = players_filepath
        self._clubs_initialized = False
        self._players_initialized = False

    def write_clubs(self, clubs: Iterator[Club]) -> None:
        mode = "a" if self._clubs_initialized else "w"
        with open(self.clubs_filepath, mode, encoding="utf-8", newline="") as handle:
            writer = csv.writer(handle, lineterminator="\n")
            if not self._clubs_initialized:
                writer.writerow(CLUB_COLUMNS)
                self._clubs_initialized = True
            for club in clubs:
                writer.writerow([
                    getattr(club, "club_id", ""),
                    getattr(club, "name", ""),
                    getattr(club, "championship", ""),
                    getattr(club, "founding_date", ""),
                    getattr(club, "city", ""),
                    getattr(club, "state", ""),
                    getattr(club, "country", ""),
                    getattr(club, "stadium", ""),
                    getattr(club, "president", ""),
                    getattr(club, "nickname", "") or "",
                    "|".join(getattr(club, "colors", []) or []),
                ])

    def write_players(self, players: Iterator[Player]) -> None:
        mode = "a" if self._players_initialized else "w"
        with open(self.players_filepath, mode, encoding="utf-8", newline="") as handle:
            writer = csv.writer(handle, lineterminator="\n")
            if not self._players_initialized:
                writer.writerow(PLAYER_COLUMNS)
                self._players_initialized = True
            for player in players:
                writer.writerow([
                    getattr(player, "club_id", ""),
                    getattr(player, "player_id", ""),
                    getattr(player, "name", ""),
                    getattr(player, "age", "") if getattr(player, "age", "") is not None else "",
                    getattr(player, "goals", "") if getattr(player, "goals", "") is not None else "",
                    getattr(player, "debut_date", ""),
                    getattr(player, "position", ""),
                    getattr(player, "shirt_number", "") or "",
                ])
