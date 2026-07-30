import json
from typing import Iterator

from batch_clubs.ports.source import ClubSource


class JsonlClubSource(ClubSource):
    def __init__(self, filepath: str) -> None:
        self.filepath = filepath

    def read(self) -> Iterator[dict]:
        with open(self.filepath, "r", encoding="utf-8") as handle:
            for line in handle:
                line = line.strip()
                if not line:
                    continue
                try:
                    data = json.loads(line)
                except json.JSONDecodeError:
                    continue

                if isinstance(data, dict):
                    yield data
