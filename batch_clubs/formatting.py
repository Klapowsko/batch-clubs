def join_colors(colors: list[str] | None) -> str:
    if not colors:
        return ""
    return "|".join(colors)
