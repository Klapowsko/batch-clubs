import pytest

from batch_clubs.models import Player
from batch_clubs.club_parser import parse_players


def test_parse_players_retorna_lista_de_jogadores_validos():
    raw_players = [
        {
            "player_id": "SCCP-10",
            "name": "Yuri Alberto",
            "age": 24,
            "goals": 7,
            "debut_date": "2024-01-10",
            "position": "Atacante",
            "shirt_number": 10,
            "nationality": "Brasil",
            "market_value": 7000000,
        },
        {
            "player_id": "SCCP-9",
            "name": "Róger Guedes",
            "age": 27,
            "goals": 5,
            "debut_date": "2023-05-01",
            "position": "Atacante",
            "shirt_number": 9,
            "nationality": "Brasil",
            "market_value": 6000000,
        },
    ]

    players = parse_players("SCCP", raw_players)

    assert len(players) == 2
    assert all(isinstance(player, Player) for player in players)
    assert players[0].club_id == "SCCP"
    assert players[1].club_id == "SCCP"


def test_parse_players_retorna_lista_vazia_quando_nao_ha_jogadores():
    players = parse_players("SCCP", [])

    assert players == []


def test_parse_players_descarta_jogadores_malformados_e_preserva_os_validos():
    raw_players = [
        {
            "player_id": "SCCP-10",
            "name": "Yuri Alberto",
            "age": 24,
            "goals": 7,
            "debut_date": "2024-01-10",
            "position": "Atacante",
            "shirt_number": 10,
            "nationality": "Brasil",
            "market_value": 7000000,
        },
        {
            "name": "Jogador sem player_id",
            "age": 22,
            "goals": 0,
            "debut_date": "2024-02-01",
            "position": "Meio-campo",
            "shirt_number": 8,
            "nationality": "Brasil",
            "market_value": 1000000,
        },
        {
            "player_id": "SCCP-7",
            "name": "Roni",
            "age": 30,
            "goals": 3,
            "debut_date": "2022-03-02",
            "position": "Atacante",
            "shirt_number": 7,
            "nationality": "Brasil",
            "market_value": 3000000,
        },
    ]

    players = parse_players("SCCP", raw_players)

    assert len(players) == 2
    assert [player.player_id for player in players] == ["SCCP-10", "SCCP-7"]


def test_parse_players_usa_campo_vazio_quando_shirt_number_esta_ausente():
    raw_players = [
        {
            "player_id": "SCCP-11",
            "name": "Gabriel Moscardo",
            "age": 18,
            "goals": 0,
            "debut_date": "2024-01-01",
            "position": "Meio-campo",
            "nationality": "Brasil",
            "market_value": 2000000,
        }
    ]

    players = parse_players("SCCP", raw_players)

    assert len(players) == 1
    assert players[0].shirt_number == ""
