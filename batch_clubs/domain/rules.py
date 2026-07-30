from datetime import datetime


def parse_date(valor: str | None) -> str:
    if valor is None:
        return ""

    if not isinstance(valor, str):
        return ""

    valor = valor.strip()
    if not valor:
        return ""

    for fmt in ("%Y-%m-%d", "%d/%m/%Y"):
        try:
            return datetime.strptime(valor, fmt).strftime("%Y-%m-%d")
        except ValueError:
            continue

    return ""


def join_colors(colors: list[str] | None) -> str:
    if not colors:
        return ""
    return "|".join(colors)
