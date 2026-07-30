import json
from typing import Iterator


def read_jsonl(filepath: str) -> Iterator[dict]:
    with open(filepath, "r", encoding="utf-8") as handle:
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
