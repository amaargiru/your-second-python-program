import pytest

from Core.game import Score


class TestScore:

    def test_initial_value(self):
        score = Score(10)
        assert score.value == 10
        assert score.diff == 10

    def test_update_value(self):
        score = Score(10)
        score.value = 14
        assert score.value == 14
        assert score.diff == 4

    def test_set_negative_value(self):
        score = Score(10)
        with pytest.raises(ValueError, match="The value of the scored points must be not less than zero."):
            score.value = -2

    def test_set_odd_value(self):
        score = Score(10)
        with pytest.raises(ValueError, match="The value of the scored points must be an even number."):
            score.value = 7

    def test_set_decreasing_value(self):
        score = Score(10)
        with pytest.raises(ValueError, match="The value of the scored points should not decrease."):
            score.value = 8

    def test_diff_calculation(self):
        score = Score(1)
        score.value = 20000
        assert score.diff == 19999

    def test_value_and_diff_after_multiple_changes(self):
        score = Score(10)
        score.value = 12
        assert score.value == 12
        assert score.diff == 2
        score.value = 16
        assert score.value == 16
        assert score.diff == 4