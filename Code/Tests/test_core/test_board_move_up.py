import pytest

from Core.game import Tile, Game


@pytest.fixture
def game():
    return Game(rows=4, columns=4)


def get_board_values(board):
    return [[tile.value for tile in row] for row in board]


def test_move_up_empty_board(game):
    game.reset()
    game.move_up()
    expected_board = [[0 for _ in range(4)] for _ in range(4)]
    assert get_board_values(game.board) == expected_board


def test_move_up_single_tile(game):
    game.reset()
    game._board = [
        [Tile(0), Tile(0), Tile(0), Tile(0)],
        [Tile(0), Tile(0), Tile(0), Tile(0)],
        [Tile(0), Tile(0), Tile(0), Tile(0)],
        [Tile(0), Tile(0), Tile(0), Tile(2)]
    ]

    game.move_up()

    expected_board = [
        [0, 0, 0, 2],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    assert get_board_values(game.board) == expected_board
    assert game.score == (0, 0)


def test_move_up_merge_tiles_var1(game):
    game.reset()
    game._board = [
        [Tile(0), Tile(2), Tile(2), Tile(4)],
        [Tile(0), Tile(2), Tile(2), Tile(4)],
        [Tile(0), Tile(0), Tile(2), Tile(0)],
        [Tile(0), Tile(2), Tile(2), Tile(8)]
    ]

    game.move_up()

    expected_board = [
        [0, 4, 4, 8],
        [0, 2, 4, 8],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    assert get_board_values(game.board) == expected_board
    assert game.score == (20, 20)


def test_move_up_merge_tiles_var2(game):
    game.reset()
    game._board = [
        [Tile(2), Tile(4), Tile(8), Tile(16)],
        [Tile(2), Tile(4), Tile(8), Tile(16)],
        [Tile(0), Tile(4), Tile(8), Tile(0)],
        [Tile(2), Tile(4), Tile(8), Tile(16)]
    ]

    game.move_up()

    expected_board = [
        [4, 8, 16, 32],
        [2, 8, 16, 16],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    assert get_board_values(game.board) == expected_board
    assert game.score == (84, 84)


def test_move_up_merge_tiles_var3(game):
    game.reset()
    game._board = [
        [Tile(2), Tile(2), Tile(4), Tile(4)],
        [Tile(4), Tile(4), Tile(4), Tile(4)],
        [Tile(2), Tile(2), Tile(2), Tile(2)],
        [Tile(0), Tile(0), Tile(0), Tile(0)]
    ]

    game.move_up()

    expected_board = [
        [2, 2, 8, 8],
        [4, 4, 2, 2],
        [2, 2, 0, 0],
        [0, 0, 0, 0]
    ]
    assert get_board_values(game.board) == expected_board
    assert game.score == (16, 16)


def test_move_up_merge_tiles_var4(game):
    game.reset()
    game._board = [
        [Tile(2), Tile(2), Tile(2), Tile(2)],
        [Tile(0), Tile(0), Tile(0), Tile(0)],
        [Tile(2), Tile(2), Tile(2), Tile(2)],
        [Tile(2), Tile(2), Tile(2), Tile(2)]
    ]

    game.move_up()

    expected_board = [
        [4, 4, 4, 4],
        [2, 2, 2, 2],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    assert get_board_values(game.board) == expected_board
    assert game.score == (16, 16)


def test_move_up_merge_tiles_var5(game):
    game.reset()
    game._board = [
        [Tile(4), Tile(4), Tile(4), Tile(4)],
        [Tile(8), Tile(8), Tile(8), Tile(8)],
        [Tile(0), Tile(16), Tile(16), Tile(32)],
        [Tile(64), Tile(64), Tile(128), Tile(128)]
    ]

    game.move_up()

    expected_board = [
        [4, 4, 4, 4],
        [8, 8, 8, 8],
        [64, 16, 16, 32],
        [0, 64, 128, 128]
    ]
    assert get_board_values(game.board) == expected_board
    assert game.score == (0, 0)


def test_move_up_merge_tiles_var6(game):
    game.reset()
    game._board = [
        [Tile(32), Tile(32), Tile(32), Tile(32)],
        [Tile(64), Tile(64), Tile(64), Tile(64)],
        [Tile(128), Tile(128), Tile(128), Tile(128)],
        [Tile(256), Tile(256), Tile(256), Tile(256)]
    ]

    game.move_up()

    expected_board = [
        [32, 32, 32, 32],
        [64, 64, 64, 64],
        [128, 128, 128, 128],
        [256, 256, 256, 256]
    ]
    assert get_board_values(game.board) == expected_board
    assert game.score == (0, 0)


def test_move_up_merge_tiles_var7(game):
    game.reset()
    game._board = [
        [Tile(2), Tile(2), Tile(4), Tile(4)],
        [Tile(2), Tile(0), Tile(4), Tile(4)],
        [Tile(8), Tile(2), Tile(0), Tile(8)],
        [Tile(256), Tile(0), Tile(256), Tile(0)]
    ]

    game.move_up()

    expected_board = [
        [4, 4, 8, 8],
        [8, 0, 256, 8],
        [256, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    assert get_board_values(game.board) == expected_board
    assert game.score == (24, 24)


def test_move_up_merge_tiles_var8(game):
    game.reset()
    game._board = [
        [Tile(8), Tile(8), Tile(16), Tile(16)],
        [Tile(64), Tile(64), Tile(0), Tile(64)],
        [Tile(32), Tile(32), Tile(0), Tile(32)],
        [Tile(256), Tile(256), Tile(0), Tile(256)]
    ]

    game.move_up()

    expected_board = [
        [8, 8, 16, 16],
        [64, 64, 0, 64],
        [32, 32, 0, 32],
        [256, 256, 0, 256]
    ]
    assert get_board_values(game.board) == expected_board
    assert game.score == (0, 0)


def test_move_up_no_move_possible(game):
    game.reset()
    game._board = [
        [Tile(2), Tile(4), Tile(8), Tile(16)],
        [Tile(32), Tile(64), Tile(128), Tile(256)],
        [Tile(512), Tile(1024), Tile(2048), Tile(4096)],
        [Tile(8192), Tile(16384), Tile(32768), Tile(65536)]
    ]

    game.move_up()

    expected_board = [
        [2, 4, 8, 16],
        [32, 64, 128, 256],
        [512, 1024, 2048, 4096],
        [8192, 16384, 32768, 65536]
    ]
    assert get_board_values(game.board) == expected_board
    assert game.score == (0, 0)