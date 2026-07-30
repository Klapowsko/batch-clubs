import json

from batch_clubs.reader import read_jsonl


def test_read_jsonl_pula_linhas_json_invalidas_e_retornas_dicionarios_validos(tmp_path):
    filepath = tmp_path / "clubs.jsonl"
    filepath.write_text(
        '{"club_id": "SCCP", "name": "Corinthians"}\n'
        '{bad json}\n'
        '{"club_id": "SEP", "name": "Palmeiras"}\n',
        encoding="utf-8",
    )

    result = list(read_jsonl(str(filepath)))

    assert result == [
        {"club_id": "SCCP", "name": "Corinthians"},
        {"club_id": "SEP", "name": "Palmeiras"},
    ]
