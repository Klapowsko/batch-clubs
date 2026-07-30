from dataclasses import dataclass, field
from typing import Any


@dataclass
class Player:
    player_id: str
    name: str
    age: int | None = None
    goals: int | None = None
    debut_date: str = ""
    position: str = ""
    shirt_number: str = ""
    nationality: str = ""
    market_value: int | None = None
    club_id: str = ""


@dataclass
class Club:
    club_id: str
    name: str
    championship: str
    founding_date: str = ""
    city: str = ""
    state: str = ""
    country: str = ""
    stadium: str = ""
    president: str = ""
    nickname: str = ""
    colors: list[str] = field(default_factory=list)
    titles: int | None = None
    players: list[Player] = field(default_factory=list)
