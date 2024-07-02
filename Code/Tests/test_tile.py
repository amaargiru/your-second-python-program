import pytest

from Core.game import Tile


class TestTile:

    def test_initial_value(self):
        tile = Tile(2)
        assert tile.value == 2

    def test_value_setter(self):
        tile = Tile(6)
        tile.value = 10
        assert tile.value == 10

    def test_set_negative_value(self):
        with pytest.raises(ValueError, match="The value of the tile must be not less than zero."):
            Tile.validate_value(-2)

    def test_set_odd_value(self):
        with pytest.raises(ValueError, match="The value of the tile must be an even number."):
            Tile.validate_value(7)
