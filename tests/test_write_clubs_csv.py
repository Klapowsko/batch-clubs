import csv

from batch_clubs.models import Club
from batch_clubs.csv_writer import write_clubs_csv


def test_write_clubs_csv_escreve_2_clubes_com_cabecalho(tmp_path):
    filepath = tmp_path / "clubs.csv"
    clubs = [
        Club(
            club_id="SCCP",
            name="Sport Club Corinthians Paulista",
            championship="SERIE A",
            founding_date="1910-09-01",
            city="São Paulo",
            state="SP",
            country="Brasil",
            stadium="Arena Corinthians",
            president="Duilio Monteiro Alves",
            nickname="Timão",
            colors=["preto", "branco"],
            titles=7,
            players=[],
        ),
        Club(
            club_id="SEP",
            name="Sociedade Esportiva Palmeiras",
            championship="SERIE A",
            founding_date="1914-08-26",
            city="São Paulo",
            state="SP",
            country="Brasil",
            stadium="Allianz Parque",
            president="Leila Pereira",
            nickname="Porco",
            colors=["verde", "branco"],
            titles=11,
            players=[],
        ),
    ]

    write_clubs_csv(str(filepath), clubs)

    with open(filepath, "r", encoding="utf-8", newline="") as handle:
        rows = list(csv.reader(handle))

    assert rows[0] == ["club_id", "name", "championship", "founding_date", "city", "state", "country", "stadium", "president", "nickname", "colors", "titles", "players"]
    assert rows[1][0] == "SCCP"
    assert rows[2][0] == "SEP"


def test_write_clubs_csv_escapa_campo_com_virgula_usando_aspas(tmp_path):
    filepath = tmp_path / "clubs.csv"
    club = Club(
        club_id="SCCP",
        name="Corinthians, Paulista",
        championship="SERIE A",
        founding_date="1910-09-01",
        city="São Paulo",
        state="SP",
        country="Brasil",
        stadium="Arena Corinthians",
        president="Duilio Monteiro Alves",
        nickname="Timão",
        colors=["preto", "branco"],
        titles=7,
        players=[],
    )

    write_clubs_csv(str(filepath), [club])

    with open(filepath, "r", encoding="utf-8", newline="") as handle:
        content = handle.read()

    assert '"Corinthians, Paulista"' in content
