import pytest
from pyfortunecookie import get_fortune, get_lucky_number, get_color

def test_get_fortune_returns_string():
    result = get_fortune()
    assert isinstance(result, str)
    assert len(result) > 0

def test_get_lucky_number_range_and_seed():
    x = get_lucky_number(seed=42, min_value=10, max_value=20)
    assert 10 <= x <= 20
    assert x == get_lucky_number(seed=42, min_value=10, max_value=20)

def test_get_lucky_number_invalid_range():
    with pytest.raises(ValueError):
        get_lucky_number(min_value=5, max_value=4)

def test_get_color_valid_palettes():
    assert get_color("soft") in {"peach","mint","lavender","sky","lemon"}
    assert get_color("bold") in {"crimson","indigo","emerald","amber","teal"}

def test_get_color_invalid_palette():
    with pytest.raises(ValueError):
        get_color("rainbow")
