import pytest

from Core.game import Game
from Core.tile import Tile


@pytest.fixture
def game():
    return Game(rows=4, columns=4)


def get_board_values(board):
    return [[tile.value for tile in row] for row in board]


def test_move_left_empty_board(game):
    game.reset()
    game.move_left()
    expected_board = [[0 for _ in range(game._columns)] for _ in range(game._rows)]
    assert get_board_values(game.board) == expected_board


# Checking the uniqueness of board elements
def test_move_left_check_uniq_ids(game):
    game.reset()
    game.move_left()

    # Counting the number of unique elements
    ids = set()
    for row in game._board:
        for item in row:
            ids.add(item)

    assert len(ids) == game._columns * game._rows


def test_move_left_single_tile(game):
    game.reset()
    game._board = [
        [Tile(0), Tile(0), Tile(0), Tile(2)],
        [Tile(0), Tile(0), Tile(0), Tile(0)],
        [Tile(0), Tile(0), Tile(0), Tile(0)],
        [Tile(0), Tile(0), Tile(0), Tile(0)]
    ]

    game.move_left()

    expected_board = [
        [2, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    assert get_board_values(game.board) == expected_board
    assert game.score == (0, 0)


def test_move_left_two_tile(game):
    game.reset()
    game._board = [
        [Tile(0), Tile(2), Tile(0), Tile(0)],
        [Tile(0), Tile(0), Tile(2), Tile(0)],
        [Tile(0), Tile(0), Tile(0), Tile(0)],
        [Tile(0), Tile(0), Tile(0), Tile(0)]
    ]

    game.move_left()

    expected_board = [
        [2, 0, 0, 0],
        [2, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    assert get_board_values(game.board) == expected_board
    assert game.score == (0, 0)


def test_move_left_merge_tiles_var1(game):
    game.reset()
    game._board = [
        [Tile(2), Tile(2), Tile(4), Tile(4)],
        [Tile(0), Tile(2), Tile(2), Tile(0)],
        [Tile(2), Tile(0), Tile(2), Tile(2)],
        [Tile(0), Tile(0), Tile(0), Tile(0)]
    ]

    game.move_left()

    expected_board = [
        [4, 8, 0, 0],
        [4, 0, 0, 0],
        [4, 2, 0, 0],
        [0, 0, 0, 0]
    ]
    assert get_board_values(game.board) == expected_board
    assert game.score == (20, 20)


def test_move_left_merge_tiles_var2(game):
    game.reset()
    game._board = [
        [Tile(4), Tile(4), Tile(0), Tile(4)],
        [Tile(2), Tile(2), Tile(2), Tile(2)],
        [Tile(8), Tile(0), Tile(8), Tile(0)],
        [Tile(16), Tile(16), Tile(16), Tile(16)]
    ]

    game.move_left()

    expected_board = [
        [8, 4, 0, 0],
        [4, 4, 0, 0],
        [16, 0, 0, 0],
        [32, 32, 0, 0]
    ]
    assert get_board_values(game.board) == expected_board
    assert game.score == (96, 96)


def test_move_left_merge_tiles_var3(game):
    game.reset()
    game._board = [
        [Tile(2), Tile(2), Tile(4), Tile(4)],
        [Tile(4), Tile(4), Tile(0), Tile(0)],
        [Tile(0), Tile(2), Tile(2), Tile(2)],
        [Tile(2), Tile(2), Tile(4), Tile(4)]
    ]

    game.move_left()

    expected_board = [
        [4, 8, 0, 0],
        [8, 0, 0, 0],
        [4, 2, 0, 0],
        [4, 8, 0, 0]
    ]
    assert get_board_values(game.board) == expected_board
    assert game.score == (36, 36)


def test_move_left_merge_tiles_var4(game):
    game.reset()
    game._board = [
        [Tile(2), Tile(2), Tile(2), Tile(2)],
        [Tile(4), Tile(4), Tile(4), Tile(4)],
        [Tile(0), Tile(4), Tile(4), Tile(8)],
        [Tile(16), Tile(16), Tile(16), Tile(16)]
    ]

    game.move_left()

    expected_board = [
        [4, 4, 0, 0],
        [8, 8, 0, 0],
        [8, 8, 0, 0],
        [32, 32, 0, 0]
    ]
    assert get_board_values(game.board) == expected_board
    assert game.score == (96, 96)


def test_move_left_merge_tiles_var5(game):
    game.reset()
    game._board = [
        [Tile(4), Tile(4), Tile(4), Tile(4)],
        [Tile(8), Tile(8), Tile(8), Tile(8)],
        [Tile(0), Tile(16), Tile(16), Tile(32)],
        [Tile(64), Tile(64), Tile(128), Tile(128)]
    ]

    game.move_left()

    expected_board = [
        [8, 8, 0, 0],
        [16, 16, 0, 0],
        [32, 32, 0, 0],
        [128, 256, 0, 0]
    ]
    assert get_board_values(game.board) == expected_board
    assert game.score == (464, 464)


def test_move_left_merge_tiles_var6(game):
    game.reset()
    game._board = [
        [Tile(32), Tile(32), Tile(32), Tile(32)],
        [Tile(64), Tile(64), Tile(64), Tile(64)],
        [Tile(128), Tile(128), Tile(128), Tile(128)],
        [Tile(256), Tile(256), Tile(256), Tile(256)]
    ]

    game.move_left()

    expected_board = [
        [64, 64, 0, 0],
        [128, 128, 0, 0],
        [256, 256, 0, 0],
        [512, 512, 0, 0]
    ]
    assert get_board_values(game.board) == expected_board
    assert game.score == (1920, 1920)


def test_move_left_merge_tiles_var7(game):
    game.reset()
    game._board = [
        [Tile(2), Tile(2), Tile(4), Tile(4)],
        [Tile(64), Tile(0), Tile(0), Tile(64)],
        [Tile(8), Tile(0), Tile(0), Tile(8)],
        [Tile(256), Tile(0), Tile(256), Tile(0)]
    ]

    game.move_left()

    expected_board = [
        [4, 8, 0, 0],
        [128, 0, 0, 0],
        [16, 0, 0, 0],
        [512, 0, 0, 0]
    ]
    assert get_board_values(game.board) == expected_board
    assert game.score == (668, 668)


def test_move_left_merge_tiles_var8(game):
    game.reset()
    game._board = [
        [Tile(8), Tile(8), Tile(0), Tile(8)],
        [Tile(64), Tile(64), Tile(0), Tile(64)],
        [Tile(32), Tile(32), Tile(0), Tile(32)],
        [Tile(256), Tile(256), Tile(0), Tile(256)]
    ]

    game.move_left()

    expected_board = [
        [16, 8, 0, 0],
        [128, 64, 0, 0],
        [64, 32, 0, 0],
        [512, 256, 0, 0]
    ]
    assert get_board_values(game.board) == expected_board
    assert game.score == (720, 720)


def test_move_left_no_move_possible(game):
    game.reset()
    game._board = [
        [Tile(2), Tile(4), Tile(8), Tile(16)],
        [Tile(32), Tile(64), Tile(128), Tile(256)],
        [Tile(512), Tile(1024), Tile(2048), Tile(4096)],
        [Tile(8192), Tile(16384), Tile(32768), Tile(65536)]
    ]

    game.move_left()

    expected_board = [
        [2, 4, 8, 16],
        [32, 64, 128, 256],
        [512, 1024, 2048, 4096],
        [8192, 16384, 32768, 65536]
    ]
    assert get_board_values(game.board) == expected_board
    assert game.score == (0, 0)
