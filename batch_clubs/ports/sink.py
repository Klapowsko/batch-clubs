from typing import Protocol

from batch_clubs.domain.models import Club, Player


class ClubSink(Protocol):
    def write_clubs(self, clubs: list[Club]) -> None:
        ...

    def write_players(self, players: list[Player]) -> None:
        ...
