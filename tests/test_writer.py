import csv

from batch_clubs.adapters.csv_sink import CsvClubSink
from batch_clubs.domain.models import Club, Player


def test_write_clubs_csv_usa_cabecalho_correspondente_a_especificacao(tmp_path):
    filepath = tmp_path / "clubs.csv"
    players_filepath = tmp_path / "players.csv"
    sink = CsvClubSink(str(filepath), str(players_filepath))
    club = Club(
        club_id="SCCP",
        name="Corinthians",
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

    sink.write_clubs(iter([club]))

    with open(filepath, "r", encoding="utf-8", newline="") as handle:
        rows = list(csv.reader(handle))

    assert rows[0] == [
        "Id do Clube",
        "Nome",
        "Campeonato",
        "Data de Fundação",
        "Cidade",
        "Estado",
        "País",
        "Estádio",
        "Presidente",
        "Apelido",
        "Cores",
    ]
    assert len(rows[1]) == 11


def test_write_players_csv_usa_cabecalho_correspondente_a_especificacao(tmp_path):
    clubs_filepath = tmp_path / "clubs.csv"
    filepath = tmp_path / "players.csv"
    sink = CsvClubSink(str(clubs_filepath), str(filepath))
    player = Player(
        player_id="SCCP-10",
        name="Yuri Alberto",
        age=24,
        goals=7,
        debut_date="2024-01-10",
        position="Atacante",
        shirt_number=10,
        nationality="Brasil",
        market_value=7000000,
        club_id="SCCP",
    )

    sink.write_players(iter([player]))

    with open(filepath, "r", encoding="utf-8", newline="") as handle:
        rows = list(csv.reader(handle))

    assert rows[0] == [
        "Id do Clube",
        "Id do Jogador",
        "Nome",
        "Idade",
        "Gols",
        "Data de Estreia",
        "Posição",
        "Número da Camisa",
    ]
