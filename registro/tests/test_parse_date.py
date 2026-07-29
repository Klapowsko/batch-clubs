import pytest

from batch_clubs.date_utils import parse_date


@pytest.mark.parametrize(
    ("valor", "esperado"),
    [
        ("2024-02-29", "2024-02-29"),
        ("29/02/2024", "2024-02-29"),
        ("", ""),
        (None, ""),
    ],
)
def test_parse_date_retorna_string_formatada_quando_valor_eh_valido_ou_vazio(valor, esperado):
    assert parse_date(valor) == esperado


def test_parse_date_retorna_string_vazia_para_data_invalida():
    assert parse_date("31-02-2020") == ""
