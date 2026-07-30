import csv
from pathlib import Path

from .models import Club, Player


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


def write_clubs_csv(filepath: str, clubs: list[Club]) -> None:
    with open(filepath, "w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, lineterminator="\n")
        writer.writerow(CLUB_COLUMNS)
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


def write_players_csv(filepath: str, players: list[Player]) -> None:
    with open(filepath, "w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, lineterminator="\n")
        writer.writerow(PLAYER_COLUMNS)
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
