from .models import Club, Player
from .rules import join_colors, parse_date


VALID_CHAMPIONSHIPS = {"SERIE A", "SERIE B"}


def parse_club(raw: dict) -> Club | None:
    if not isinstance(raw, dict):
        return None

    required_fields = ["club_id", "name", "championship", "founding_date"]
    if any(field not in raw or raw.get(field) in (None, "") for field in required_fields):
        return None

    championship = str(raw.get("championship", "")).strip().upper()
    if championship not in VALID_CHAMPIONSHIPS:
        return None

    nickname = str(raw.get("nickname") or "")
    colors = raw.get("colors") or []
    if not isinstance(colors, list):
        colors = []

    raw_players = raw.get("players") or []
    if not isinstance(raw_players, list):
        raw_players = []

    players = parse_players(str(raw.get("club_id", "")), raw_players)

    return Club(
        club_id=str(raw.get("club_id", "")),
        name=str(raw.get("name", "")),
        championship=championship,
        founding_date=parse_date(str(raw.get("founding_date", ""))),
        city=str(raw.get("city") or ""),
        state=str(raw.get("state") or ""),
        country=str(raw.get("country") or ""),
        stadium=str(raw.get("stadium") or ""),
        president=str(raw.get("president") or ""),
        nickname=nickname,
        colors=[str(color) for color in colors],
        titles=int(raw.get("titles")) if raw.get("titles") is not None else None,
        players=players,
    )


def parse_players(club_id: str, raw_players: list[dict]) -> list[Player]:
    if not isinstance(raw_players, list):
        return []

    players: list[Player] = []
    for raw in raw_players:
        if not isinstance(raw, dict):
            continue

        player_id = raw.get("player_id")
        if not player_id:
            continue

        shirt_number = raw.get("shirt_number")
        if shirt_number is None:
            shirt_number = ""
        else:
            shirt_number = str(shirt_number)

        player = Player(
            player_id=str(player_id),
            name=str(raw.get("name") or ""),
            age=int(raw.get("age")) if raw.get("age") is not None else None,
            goals=int(raw.get("goals")) if raw.get("goals") is not None else None,
            debut_date=parse_date(str(raw.get("debut_date") or "")),
            position=str(raw.get("position") or ""),
            shirt_number=shirt_number,
            nationality=str(raw.get("nationality") or ""),
            market_value=int(raw.get("market_value")) if raw.get("market_value") is not None else None,
            club_id=str(club_id),
        )
        players.append(player)

    return players