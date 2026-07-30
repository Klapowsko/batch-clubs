from batch_clubs.domain.rules import parse_optional_int


def test_parse_optional_int_retorna_int_para_valor_valido():
    assert parse_optional_int("42") == 42


def test_parse_optional_int_retorna_none_para_none():
    assert parse_optional_int(None) is None


def test_parse_optional_int_retorna_none_para_valor_nao_numerico():
    assert parse_optional_int("abc") is None
