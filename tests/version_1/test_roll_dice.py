import pytest
from ten_thousand.game_logic import GameLogic

pytestmark = [pytest.mark.version_1]


# @pytest.mark.skip("TODO")
def test_1_dice():
    values = GameLogic.roll_dice(1)
    assert len(values) == 1
    value = values[0]
    assert 1 <= value <= 6


# @pytest.mark.skip("TODO")
def test_2_dice():
    values = GameLogic.roll_dice(2)
    assert len(values) == 2

    for value in values:
        assert 1 <= value <= 6


# @pytest.mark.skip("TODO")
def test_3_dice():
    values = GameLogic.roll_dice(3)
    assert len(values) == 3

    for value in values:
        assert 1 <= value <= 6


# @pytest.mark.skip("TODO")
def test_4_dice():
    values = GameLogic.roll_dice(4)
    assert len(values) == 4

    for value in values:
        assert 1 <= value <= 6


# @pytest.mark.skip("TODO")
def test_5_dice():
    values = GameLogic.roll_dice(5)
    assert len(values) == 5

    for value in values:
        assert 1 <= value <= 6


# @pytest.mark.skip("TODO")
def test_6_dice():
    values = GameLogic.roll_dice(6)
    assert len(values) == 6

    for value in values:
        assert 1 <= value <= 6
