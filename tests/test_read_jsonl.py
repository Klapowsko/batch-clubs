import json

from batch_clubs.adapters.jsonl_source import JsonlClubSource


def test_read_jsonl_pula_linhas_json_invalidas_e_retornas_dicionarios_validos(tmp_path):
    filepath = tmp_path / "clubs.jsonl"
    filepath.write_text(
        '{"club_id": "SCCP", "name": "Corinthians"}\n'
        '{bad json}\n'
        '{"club_id": "SEP", "name": "Palmeiras"}\n',
        encoding="utf-8",
    )

    source = JsonlClubSource(str(filepath))
    result = list(source.read())

    assert result == [
        {"club_id": "SCCP", "name": "Corinthians"},
        {"club_id": "SEP", "name": "Palmeiras"},
    ]
