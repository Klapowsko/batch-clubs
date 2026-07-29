import pytest

from batch_clubs.color_utils import join_colors


@pytest.mark.parametrize(
    ("colors", "expected"),
    [
        (["red", "green", "blue"], "red|green|blue"),
        (["red"], "red"),
        ([], ""),
        (None, ""),
    ],
)
def test_join_colors_returns_expected_string(colors, expected):
    assert join_colors(colors) == expected
