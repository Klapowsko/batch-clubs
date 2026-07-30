from typing import Iterator, Protocol


class ClubSource(Protocol):
    def read(self) -> Iterator[dict]:
        ...
