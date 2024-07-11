import pytest

from Core.game import Tile, Game


@pytest.fixture
def game():
    return Game(rows=4, columns=4)


def get_board_values(board):
    return [[tile.value for tile in row] for row in board]


def test_move_down_empty_board(game):
    game.reset()
    game.move_down()
    expected_board = [[0 for _ in range(game._columns)] for _ in range(game._rows)]
    assert get_board_values(game.board) == expected_board


# Checking the uniqueness of board elements
def test_move_down_check_uniq_ids(game):
    game.reset()
    game.move_down()

    # Counting the number of unique elements
    ids = set()
    for row in game._board:
        for item in row:
            ids.add(item)

    assert len(ids) == game._columns * game._rows


def test_move_down_single_tile(game):
    game.reset()
    game._board = [
        [Tile(0), Tile(0), Tile(0), Tile(2)],
        [Tile(0), Tile(0), Tile(0), Tile(0)],
        [Tile(0), Tile(0), Tile(0), Tile(0)],
        [Tile(0), Tile(0), Tile(0), Tile(0)]
    ]

    game.move_down()

    expected_board = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 2]
    ]
    assert get_board_values(game.board) == expected_board
    assert game.score == (0, 0)


def test_move_down_merge_tiles_var1(game):
    game.reset()
    game._board = [
        [Tile(2), Tile(2), Tile(4), Tile(4)],
        [Tile(0), Tile(2), Tile(2), Tile(0)],
        [Tile(0), Tile(0), Tile(2), Tile(2)],
        [Tile(0), Tile(2), Tile(0), Tile(0)]
    ]

    game.move_down()

    expected_board = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 2, 4, 4],
        [2, 4, 4, 2]
    ]
    assert get_board_values(game.board) == expected_board
    assert game.score == (8, 8)


def test_move_down_merge_tiles_var2(game):
    game.reset()
    game._board = [
        [Tile(2), Tile(2), Tile(0), Tile(2)],
        [Tile(0), Tile(0), Tile(2), Tile(0)],
        [Tile(2), Tile(2), Tile(2), Tile(2)],
        [Tile(2), Tile(2), Tile(2), Tile(2)]
    ]

    game.move_down()

    expected_board = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [2, 2, 2, 2],
        [4, 4, 4, 4]
    ]
    assert get_board_values(game.board) == expected_board
    assert game.score == (16, 16)


def test_move_down_merge_tiles_var3(game):
    game.reset()
    game._board = [
        [Tile(8), Tile(8), Tile(8), Tile(8)],
        [Tile(8), Tile(8), Tile(8), Tile(8)],
        [Tile(0), Tile(16), Tile(16), Tile(32)],
        [Tile(64), Tile(64), Tile(128), Tile(128)]
    ]

    game.move_down()

    expected_board = [
        [0, 0, 0, 0],
        [0, 16, 16, 16],
        [16, 16, 16, 32],
        [64, 64, 128, 128]
    ]
    assert get_board_values(game.board) == expected_board
    assert game.score == (64, 64)


def test_move_down_merge_tiles_var4(game):
    game.reset()
    game._board = [
        [Tile(16), Tile(16), Tile(32), Tile(32)],
        [Tile(64), Tile(16), Tile(32), Tile(32)],
        [Tile(128), Tile(0), Tile(128), Tile(128)],
        [Tile(128), Tile(0), Tile(256), Tile(0)]
    ]

    game.move_down()

    expected_board = [
        [0, 0, 0, 0],
        [16, 0, 64, 0],
        [64, 0, 128, 64],
        [256, 32, 256, 128]
    ]
    assert get_board_values(game.board) == expected_board
    assert game.score == (416, 416)


def test_move_down_merge_tiles_var5(game):
    game.reset()
    game._board = [
        [Tile(8), Tile(16), Tile(32), Tile(64)],
        [Tile(128), Tile(128), Tile(128), Tile(128)],
        [Tile(128), Tile(128), Tile(128), Tile(128)],
        [Tile(256), Tile(256), Tile(256), Tile(256)]
    ]

    game.move_down()

    expected_board = [
        [0, 0, 0, 0],
        [8, 16, 32, 64],
        [256, 256, 256, 256],
        [256, 256, 256, 256]
    ]
    assert get_board_values(game.board) == expected_board
    assert game.score == (1024, 1024)


def test_move_down_merge_tiles_var6(game):
    game.reset()
    game._board = [
        [Tile(8), Tile(8), Tile(8), Tile(8)],
        [Tile(8), Tile(8), Tile(8), Tile(8)],
        [Tile(64), Tile(64), Tile(64), Tile(64)],
        [Tile(64), Tile(64), Tile(64), Tile(64)]
    ]

    game.move_down()

    expected_board = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [16, 16, 16, 16],
        [128, 128, 128, 128]
    ]
    assert get_board_values(game.board) == expected_board
    assert game.score == (576, 576)


def test_move_down_merge_tiles_var7(game):
    game.reset()
    game._board = [
        [Tile(256), Tile(256), Tile(256), Tile(256)],
        [Tile(0), Tile(0), Tile(0), Tile(0)],
        [Tile(256), Tile(256), Tile(256), Tile(256)],
        [Tile(0), Tile(0), Tile(0), Tile(0)]
    ]

    game.move_down()

    expected_board = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [512, 512, 512, 512]
    ]
    assert get_board_values(game.board) == expected_board
    assert game.score == (2048, 2048)


def test_move_down_merge_tiles_var8(game):
    game.reset()
    game._board = [
        [Tile(4), Tile(4), Tile(4), Tile(4)],
        [Tile(4), Tile(4), Tile(4), Tile(4)],
        [Tile(4), Tile(4), Tile(4), Tile(4)],
        [Tile(4), Tile(4), Tile(4), Tile(4)]
    ]

    game.move_down()

    expected_board = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [8, 8, 8, 8],
        [8, 8, 8, 8]
    ]
    assert get_board_values(game.board) == expected_board
    assert game.score == (64, 64)


def test_move_down_no_move_possible(game):
    game.reset()
    game._board = [
        [Tile(2), Tile(4), Tile(8), Tile(16)],
        [Tile(32), Tile(64), Tile(128), Tile(256)],
        [Tile(512), Tile(1024), Tile(2048), Tile(4096)],
        [Tile(8192), Tile(16384), Tile(32768), Tile(65536)]
    ]

    game.move_down()

    expected_board = [
        [2, 4, 8, 16],
        [32, 64, 128, 256],
        [512, 1024, 2048, 4096],
        [8192, 16384, 32768, 65536]
    ]
    assert get_board_values(game.board) == expected_board
    assert game.score == (0, 0)
