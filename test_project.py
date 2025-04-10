import pytest
from unittest.mock import patch
from project import calc_kcal, get_activity, get_weight, get_name


def test_calc_kcal():
    assert calc_kcal(10, "very") == 731
    assert calc_kcal(10, "normal") == 669
    assert calc_kcal(10, "lightly") == 607
    assert calc_kcal(20, "very") == 1229
    assert calc_kcal(20, "normal") == 1125
    assert calc_kcal(20, "lightly") == 1021


@patch("builtins.input", side_effect=["normal"])
def test_get_activity(mock_input):
    assert get_activity("Buddy") == "normal"


@patch("builtins.input", side_effect=["invalid", "very"])
def test_get_activity_invalid(mock_input):
    assert get_activity("Buddy") == "very"


@patch("builtins.input", side_effect=["15"])
def test_get_weight(mock_input):
    assert get_weight("Buddy") == 15.0


@patch("builtins.input", side_effect=["invalid", "20"])
def test_get_weight_invalid(mock_input):
    assert get_weight("Buddy") == 20.0


@patch("builtins.input", side_effect=["Buddy"])
def test_get_name(mock_input):
    assert get_name() == "Buddy"


@patch("builtins.input", side_effect=["1234", "Charlie"])
def test_get_name_invalid(mock_input):
    assert get_name() == "Charlie"
