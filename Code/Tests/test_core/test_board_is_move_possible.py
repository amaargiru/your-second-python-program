import pytest

from Core.game import Tile, Game


@pytest.fixture
def game():
    return Game(rows=4, columns=4)


def get_board_values(board):
    return [[tile.value for tile in row] for row in board]


# Ensures that a move is possible on an empty board
def test_is_move_possible_empty_board(game):
    game.reset()
    assert game._is_move_possible() is True


# Ensures that a move is possible when there is a single tile on the board
def test_is_move_possible_single_tile(game):
    game.reset()
    game._board = [
        [Tile(0), Tile(0), Tile(0), Tile(2)],
        [Tile(0), Tile(0), Tile(0), Tile(0)],
        [Tile(0), Tile(0), Tile(0), Tile(0)],
        [Tile(0), Tile(0), Tile(0), Tile(0)]
    ]
    assert game._is_move_possible() is True


# Ensures that a move is possible if there are adjacent tiles with the same value on a full board
def test_is_move_possible_full_board_with_move(game):
    game.reset()
    game._board = [
        [Tile(2), Tile(4), Tile(8), Tile(16)],
        [Tile(32), Tile(64), Tile(128), Tile(256)],
        [Tile(512), Tile(1024), Tile(1024), Tile(4096)],
        [Tile(8192), Tile(16384), Tile(32768), Tile(65536)]
    ]
    assert game._is_move_possible() is True


# Ensures that no move is possible on a full board with no adjacent tiles of the same value
def test_is_move_possible_full_board_no_move_possible(game):
    game.reset()
    game._board = [
        [Tile(2), Tile(4), Tile(8), Tile(16)],
        [Tile(32), Tile(64), Tile(128), Tile(256)],
        [Tile(512), Tile(1024), Tile(2048), Tile(4096)],
        [Tile(8192), Tile(16384), Tile(32768), Tile(65536)]
    ]
    assert game._is_move_possible() is False


# Ensures that a move is possible if there is at least one zero tile on the board
def test_is_move_possible_almost_full_board_with_zero_tile(game):
    game.reset()
    game._board = [
        [Tile(2), Tile(4), Tile(8), Tile(16)],
        [Tile(32), Tile(64), Tile(128), Tile(256)],
        [Tile(512), Tile(1024), Tile(2048), Tile(4096)],
        [Tile(8192), Tile(16384), Tile(32768), Tile(0)]
    ]
    assert game._is_move_possible() is True


# Ensures that a move is possible when there are adjacent tiles with the same value in various configurations
def test_is_move_possible_board_with_adjacent_equal_tiles(game):
    game.reset()
    game._board = [
        [Tile(2), Tile(2), Tile(8), Tile(16)],
        [Tile(32), Tile(64), Tile(128), Tile(256)],
        [Tile(512), Tile(1024), Tile(2048), Tile(4096)],
        [Tile(8192), Tile(16384), Tile(32768), Tile(65536)]
    ]
    assert game._is_move_possible() is True

    game._board = [
        [Tile(2), Tile(4), Tile(8), Tile(16)],
        [Tile(32), Tile(64), Tile(128), Tile(256)],
        [Tile(512), Tile(1024), Tile(2048), Tile(4096)],
        [Tile(8192), Tile(16384), Tile(32768), Tile(32768)]
    ]
    assert game._is_move_possible() is True

    game._board = [
        [Tile(2), Tile(4), Tile(8), Tile(16)],
        [Tile(2), Tile(64), Tile(128), Tile(256)],
        [Tile(512), Tile(1024), Tile(2048), Tile(4096)],
        [Tile(8192), Tile(16384), Tile(32768), Tile(65536)]
    ]
    assert game._is_move_possible() is True

    game._board = [
        [Tile(2), Tile(4), Tile(8), Tile(16)],
        [Tile(32), Tile(64), Tile(128), Tile(16)],
        [Tile(512), Tile(1024), Tile(2048), Tile(4096)],
        [Tile(8192), Tile(16384), Tile(32768), Tile(65536)]
    ]
    assert game._is_move_possible() is True


# Ensures that a move is possible when there are several zero tiles on the board
def test_is_move_possible_board_with_near_zero_tiles(game):
    game.reset()
    game._board = [
        [Tile(0), Tile(0), Tile(0), Tile(0)],
        [Tile(0), Tile(0), Tile(0), Tile(0)],
        [Tile(0), Tile(0), Tile(0), Tile(0)],
        [Tile(0), Tile(0), Tile(0), Tile(2)]
    ]
    assert game._is_move_possible() is True

    game._board = [
        [Tile(2), Tile(0), Tile(0), Tile(0)],
        [Tile(0), Tile(0), Tile(0), Tile(0)],
        [Tile(0), Tile(0), Tile(0), Tile(0)],
        [Tile(0), Tile(0), Tile(0), Tile(0)]
    ]
    assert game._is_move_possible() is True

    game._board = [
        [Tile(0), Tile(0), Tile(0), Tile(0)],
        [Tile(0), Tile(0), Tile(0), Tile(0)],
        [Tile(0), Tile(0), Tile(0), Tile(0)],
        [Tile(0), Tile(0), Tile(2), Tile(0)]
    ]
    assert game._is_move_possible() is True
