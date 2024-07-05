import pytest

from Core.game import Tile, Game


@pytest.fixture
def game():
    return Game(rows=4, columns=4)


def get_board_values(board):
    return [[tile.value for tile in row] for row in board]


def test_move_right_empty_board(game):
    game.reset()
    game._board = [
        [Tile(0), Tile(0), Tile(0), Tile(0)],
        [Tile(0), Tile(0), Tile(0), Tile(0)],
        [Tile(0), Tile(0), Tile(0), Tile(0)],
        [Tile(0), Tile(0), Tile(0), Tile(0)]
    ]

    game.move_right()

    expected_board = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]

    assert get_board_values(game.board) == expected_board

    assert game.score == (0, 0)


def test_move_right_single_tile(game):
    game.reset()
    game._board = [
        [Tile(2), Tile(0), Tile(0), Tile(0)],
        [Tile(0), Tile(0), Tile(0), Tile(0)],
        [Tile(0), Tile(0), Tile(0), Tile(0)],
        [Tile(0), Tile(0), Tile(0), Tile(0)]
    ]

    game.move_right()

    expected_board = [
        [0, 0, 0, 2],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    assert get_board_values(game.board) == expected_board
    assert game.score == (0, 0)


def test_move_right_merge_tiles_var1(game):
    game.reset()
    game._board = [
        [Tile(0), Tile(0), Tile(2), Tile(2)],
        [Tile(0), Tile(4), Tile(4), Tile(0)],
        [Tile(2), Tile(2), Tile(2), Tile(2)],
        [Tile(0), Tile(0), Tile(0), Tile(0)]
    ]

    game.move_right()

    expected_board = [
        [0, 0, 0, 4],
        [0, 0, 0, 8],
        [0, 0, 4, 4],
        [0, 0, 0, 0]
    ]

    assert get_board_values(game.board) == expected_board

    assert game.score == (20, 20)


def test_move_right_merge_tiles_var2(game):
    game.reset()
    game._board = [
        [Tile(2), Tile(4), Tile(8), Tile(16)],
        [Tile(0), Tile(4), Tile(0), Tile(8)],
        [Tile(2), Tile(0), Tile(2), Tile(2)],
        [Tile(8), Tile(8), Tile(8), Tile(8)]
    ]

    game.move_right()

    expected_board = [
        [2, 4, 8, 16],
        [0, 0, 4, 8],
        [0, 0, 2, 4],
        [0, 0, 16, 16]
    ]

    assert get_board_values(game.board) == expected_board

    assert game.score == (36, 36)


def test_move_right_merge_tiles_var3(game):
    game.reset()
    game._board = [
        [Tile(2), Tile(2), Tile(4), Tile(4)],
        [Tile(4), Tile(4), Tile(8), Tile(8)],
        [Tile(16), Tile(16), Tile(32), Tile(0)],
        [Tile(0), Tile(0), Tile(0), Tile(0)]
    ]

    game.move_right()

    expected_board = [
        [0, 0, 4, 8],
        [0, 0, 8, 16],
        [0, 0, 32, 32],
        [0, 0, 0, 0]
    ]

    assert get_board_values(game.board) == expected_board

    assert game.score == (68, 68)


def test_move_right_merge_tiles_var4(game):
    game.reset()
    game._board = [
        [Tile(8), Tile(0), Tile(0), Tile(8)],
        [Tile(0), Tile(4), Tile(4), Tile(0)],
        [Tile(16), Tile(16), Tile(32), Tile(32)],
        [Tile(2), Tile(2), Tile(0), Tile(0)]
    ]

    game.move_right()

    expected_board = [
        [0, 0, 0, 16],
        [0, 0, 0, 8],
        [0, 0, 32, 64],
        [0, 0, 0, 4]
    ]

    assert get_board_values(game.board) == expected_board

    assert game.score == (124, 124)


def test_move_right_merge_tiles_var5(game):
    game.reset()
    game._board = [
        [Tile(2), Tile(2), Tile(4), Tile(4)],
        [Tile(8), Tile(8), Tile(16), Tile(16)],
        [Tile(32), Tile(32), Tile(64), Tile(64)],
        [Tile(128), Tile(128), Tile(1_048_576), Tile(1_048_576)]
    ]

    game.move_right()

    expected_board = [
        [0, 0, 4, 8],
        [0, 0, 16, 32],
        [0, 0, 64, 128],
        [0, 0, 256, 2_097_152]
    ]

    assert get_board_values(game.board) == expected_board

    assert game.score == (2_097_660, 2_097_660)


def test_move_right_merge_tiles_var6(game):
    game.reset()
    game._board = [
        [Tile(0), Tile(2), Tile(2), Tile(4)],
        [Tile(0), Tile(0), Tile(4), Tile(4)],
        [Tile(8), Tile(0), Tile(0), Tile(8)],
        [Tile(2), Tile(0), Tile(0), Tile(2)]
    ]

    game.move_right()

    expected_board = [
        [0, 0, 4, 4],
        [0, 0, 0, 8],
        [0, 0, 0, 16],
        [0, 0, 0, 4]
    ]

    assert get_board_values(game.board) == expected_board

    assert game.score == (32, 32)


def test_move_right_merge_tiles_var7(game):
    game.reset()
    game._board = [
        [Tile(2), Tile(2), Tile(32), Tile(32)],
        [Tile(8), Tile(8), Tile(4), Tile(4)],
        [Tile(64), Tile(64), Tile(128), Tile(128)],
        [Tile(256), Tile(256), Tile(512), Tile(512)]
    ]

    game.move_right()

    expected_board = [
        [0, 0, 4, 64],
        [0, 0, 16, 8],
        [0, 0, 128, 256],
        [0, 0, 512, 1024]
    ]

    assert get_board_values(game.board) == expected_board

    assert game.score == (2012, 2012)


def test_move_right_merge_tiles_var8(game):
    game.reset()
    game._board = [
        [Tile(2), Tile(2), Tile(2), Tile(0)],
        [Tile(8), Tile(8), Tile(8), Tile(0)],
        [Tile(16), Tile(16), Tile(16), Tile(0)],
        [Tile(32), Tile(32), Tile(32), Tile(0)]
    ]

    game.move_right()

    expected_board = [
        [0, 0, 2, 4],
        [0, 0, 8, 16],
        [0, 0, 16, 32],
        [0, 0, 32, 64]
    ]

    assert get_board_values(game.board) == expected_board

    assert game.score == (116, 116)


def test_move_right_no_move_possible(game):
    game.reset()
    game._board = [
        [Tile(2), Tile(4), Tile(8), Tile(16)],
        [Tile(32), Tile(64), Tile(128), Tile(256)],
        [Tile(512), Tile(1024), Tile(2048), Tile(4096)],
        [Tile(8192), Tile(16384), Tile(32768), Tile(65536)]
    ]

    game.move_right()

    expected_board = [
        [2, 4, 8, 16],
        [32, 64, 128, 256],
        [512, 1024, 2048, 4096],
        [8192, 16384, 32768, 65536]
    ]

    assert get_board_values(game.board) == expected_board

    assert game.score == (0, 0)
