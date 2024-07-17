import pytest

from Core.game import Game
from Core.tile import Tile


@pytest.fixture
def game():
    return Game(rows=4, columns=4)


def get_board_values(board):
    return [[tile.value for tile in row] for row in board]


def count_empty_tiles(board):
    return sum(1 for row in board for tile in row if tile.value == 0)


def count_specific_value_tiles(board, value):
    return sum(1 for row in board for tile in row if tile.value == value)


# Checks if a random tile is added to an empty board and if the board now contains exactly one new tile of value 2 or 4
def test_add_random_tile_empty_board(game):
    game.reset()
    num_empty_before = count_empty_tiles(game.board)

    game.add_random_tile()

    num_empty_after = count_empty_tiles(game.board)
    assert num_empty_after == num_empty_before - 1

    num_twos = count_specific_value_tiles(game.board, 2)
    num_fours = count_specific_value_tiles(game.board, 4)
    assert num_twos + num_fours == 1
    assert game.score == (0, 0)


def test_add_random_tile_almost_empty_board(game):
    game.reset()
    game._board = [
        [Tile(2), Tile(0), Tile(0), Tile(0)],
        [Tile(0), Tile(2), Tile(0), Tile(0)],
        [Tile(0), Tile(0), Tile(0), Tile(0)],
        [Tile(0), Tile(0), Tile(0), Tile(0)]
    ]
    num_empty_before = count_empty_tiles(game.board)
    num_twos_before = count_specific_value_tiles(game.board, 2)
    num_fours_before = count_specific_value_tiles(game.board, 4)

    game.add_random_tile()

    num_empty_after = count_empty_tiles(game.board)
    assert num_empty_after == num_empty_before - 1

    num_twos_after = count_specific_value_tiles(game.board, 2)
    num_fours_after = count_specific_value_tiles(game.board, 4)

    assert num_twos_before + num_fours_before == num_twos_after + num_fours_after - 1
    assert game.score == (0, 0)


# Checks if a random tile is added to a partially filled board and if the board now contains exactly one new tile of value 2 or 4
def test_add_random_tile_partially_filled_board(game):
    game.reset()
    game._board = [
        [Tile(2), Tile(4), Tile(8), Tile(16)],
        [Tile(32), Tile(0), Tile(0), Tile(256)],
        [Tile(512), Tile(0), Tile(2048), Tile(4096)],
        [Tile(8192), Tile(16384), Tile(0), Tile(65536)]
    ]
    num_empty_before = count_empty_tiles(game.board)
    num_twos_before = count_specific_value_tiles(game.board, 2)
    num_fours_before = count_specific_value_tiles(game.board, 4)

    game.add_random_tile()

    num_empty_after = count_empty_tiles(game.board)
    assert num_empty_after == num_empty_before - 1

    num_twos_after = count_specific_value_tiles(game.board, 2)
    num_fours_after = count_specific_value_tiles(game.board, 4)

    assert num_twos_before + num_fours_before == num_twos_after + num_fours_after - 1
    assert game.score == (0, 0)


# Checks if a random tile is added to an almost full board and if the board now contains exactly one new tile of value 2 or 4
def test_add_random_tile_almost_full_board(game):
    game.reset()
    game._board = [
        [Tile(2), Tile(4), Tile(8), Tile(16)],
        [Tile(32), Tile(64), Tile(128), Tile(256)],
        [Tile(512), Tile(1024), Tile(2048), Tile(4096)],
        [Tile(8192), Tile(16384), Tile(32768), Tile(0)]
    ]
    num_empty_before = count_empty_tiles(game.board)

    game.add_random_tile()

    num_empty_after = count_empty_tiles(game.board)
    assert num_empty_after == num_empty_before - 1

    num_twos = count_specific_value_tiles(game.board, 2)
    num_fours = count_specific_value_tiles(game.board, 4)
    assert num_twos + num_fours == 3
    assert game.score == (0, 0)


# Ensures no new tile is added if the board is full
def test_add_random_tile_full_board(game):
    game.reset()
    game._board = [
        [Tile(2), Tile(4), Tile(8), Tile(16)],
        [Tile(32), Tile(64), Tile(128), Tile(256)],
        [Tile(512), Tile(1024), Tile(2048), Tile(4096)],
        [Tile(8192), Tile(16384), Tile(32768), Tile(65536)]
    ]
    added = game.add_random_tile()

    assert added is False
    assert game.score == (0, 0)


# Ensures the random tile is added to the only possible place left in the nearly full board and then the second only possible place left
def test_add_random_tile_add_only_possible_move(game):
    game.reset()
    game._board = [
        [Tile(2), Tile(2), Tile(4), Tile(4)],
        [Tile(8), Tile(8), Tile(16), Tile(16)],
        [Tile(32), Tile(32), Tile(64), Tile(64)],
        [Tile(128), Tile(128), Tile(0), Tile(0)]
    ]

    num_empty_before = count_empty_tiles(game.board)
    game.add_random_tile()
    num_empty_after = count_empty_tiles(game.board)
    assert num_empty_after == num_empty_before - 1

    num_twos = count_specific_value_tiles(game.board, 2)
    num_fours = count_specific_value_tiles(game.board, 4)
    assert num_twos + num_fours == 5

    game.add_random_tile()
    num_empty_after = count_empty_tiles(game.board)
    assert num_empty_after == 0

    assert game.score == (0, 0)


# Runs the method enough times to statistically verify that both 2s and 4s are being added over multiple runs
def test_add_random_tile_all_possible_values(game):
    # Ensure that both 2 and 4 values are being added
    game.reset()
    twos, fours = 0, 0
    for _ in range(100):  # Run enough iterations to capture the probabilities
        game.reset()
        game.add_random_tile()
        twos += count_specific_value_tiles(game.board, 2)
        fours += count_specific_value_tiles(game.board, 4)

    assert twos > 0
    assert fours > 0
    assert game.score == (0, 0)
