from leap import is_leap


def test_2024_is_leap_year():
    assert is_leap(2024) is True


def test_1900_is_not_leap_year():
    assert is_leap(1900) is False


def test_2000_is_leap_year():
    assert is_leap(2000) is True


import pytest


@pytest.mark.parametrize("year, expected", [
    (2024, True),
    (2023, False),
    (2000, True),
    (1900, False),
    (2028, True),
    (2100, False),
])
def test_is_leap_parametrized(year, expected):
    assert is_leap(year) is expected


@pytest.mark.parametrize("year", [0, -1, -100])
def test_invalid_year_raises_value_error(year):
    with pytest.raises(ValueError):
        is_leap(year)
