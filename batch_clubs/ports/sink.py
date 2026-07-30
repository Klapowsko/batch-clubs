from typing import Iterator, Protocol

from batch_clubs.domain.models import Club, Player


class ClubSink(Protocol):
    def write_clubs(self, clubs: Iterator[Club]) -> None:
        ...

    def write_players(self, players: Iterator[Player]) -> None:
        ...
