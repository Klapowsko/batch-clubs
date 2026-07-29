import pytest

from batch_clubs.models import Club
from batch_clubs.club_parser import parse_club


@pytest.fixture
def raw_club_valid():
    return {
        "club_id": "SCCP",
        "name": "Sport Club Corinthians Paulista",
        "championship": "SERIE A",
        "founding_date": "1910-09-01",
        "city": "São Paulo",
        "state": "SP",
        "country": "Brasil",
        "stadium": "Arena Corinthians",
        "president": "Duilio Monteiro Alves",
        "nickname": "Timão",
        "colors": ["preto", "branco"],
        "titles": 7,
        "players": [{
            "player_id": "SCCP-10",
            "name": "Yuri Alberto",
            "age": 24,
            "goals": 7,
            "debut_date": "2024-01-10",
            "position": "Atacante",
            "shirt_number": 10,
            "nationality": "Brasil",
            "market_value": 7000000,
        }],
    }


def test_parse_club_retorna_club_valido_para_campeonato_serie_a(raw_club_valid):
    club = parse_club(raw_club_valid)

    assert isinstance(club, Club)
    assert club.club_id == "SCCP"
    assert club.championship == "SERIE A"
    assert club.nickname == "Timão"


def test_parse_club_retorna_none_para_campeonato_invalido():
    raw = {
        "club_id": "NAC",
        "name": "Nacional Atlético Clube",
        "championship": "SERIE C",
        "founding_date": "1919-06-04",
        "city": "São Paulo",
        "state": "SP",
        "country": "Brasil",
        "stadium": "Nicolau Alayon",
        "president": "Antônio Carlos",
        "nickname": "Naça",
        "colors": ["azul", "branco", "vermelho"],
        "titles": 0,
        "players": [],
    }

    assert parse_club(raw) is None


def test_parse_club_gera_nickname_vazio_quando_falta_nickname(raw_club_valid):
    raw_club_valid.pop("nickname")

    club = parse_club(raw_club_valid)

    assert isinstance(club, Club)
    assert club.nickname == ""


def test_parse_club_retorna_club_valido_sem_players_quando_lista_nao_existe():
    raw = {
        "club_id": "AVA",
        "name": "Avaí Futebol Clube",
        "championship": "SERIE B",
        "founding_date": "1923-09-01",
        "city": "Florianópolis",
        "state": "SC",
        "country": "Brasil",
        "stadium": "Ressacada",
        "president": "Júlio Heerdt",
        "nickname": "Leão da Ilha",
        "colors": ["azul", "branco"],
        "titles": 0,
    }

    club = parse_club(raw)

    assert isinstance(club, Club)
    assert club.players == []


def test_parse_club_retorna_none_quando_campo_obrigatorio_esta_ausente():
    raw = {
        "name": "Cruzeiro Esporte Clube",
        "championship": "SERIE A",
        "founding_date": "1921-01-02",
        "city": "Belo Horizonte",
        "state": "MG",
        "country": "Brasil",
        "stadium": "Mineirão",
        "president": "Pedro Lourenço, Filho",
        "nickname": "Raposa",
        "colors": ["azul", "branco"],
        "titles": 4,
        "players": [],
    }

    assert parse_club(raw) is None
