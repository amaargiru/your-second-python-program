import pytest

from Core.game import Tile, Game


@pytest.fixture
def game():
    return Game(rows=4, columns=4)


def get_board_values(board):
    return [[tile.value for tile in row] for row in board]


def test_move_right_simple_merge(game):
    game.reset()
    game._board = [
        [Tile(0), Tile(0), Tile(2), Tile(2)],
        [Tile(0), Tile(4), Tile(4), Tile(0)],
        [Tile(2), Tile(2), Tile(2), Tile(2)],
        [Tile(0), Tile(0), Tile(0), Tile(0)],
    ]

    game.move_right()

    expected_board = [
        [0, 0, 0, 4],
        [0, 0, 0, 8],
        [0, 0, 4, 4],
        [0, 0, 0, 0],
    ]

    assert get_board_values(game.board) == expected_board

    assert game.score == (20, 4)


def test_move_right_complex_merge_var1(game):
    game.reset()
    game._board = [
        [Tile(2), Tile(4), Tile(8), Tile(16)],
        [Tile(0), Tile(4), Tile(0), Tile(8)],
        [Tile(2), Tile(0), Tile(2), Tile(2)],
        [Tile(8), Tile(8), Tile(8), Tile(8)],
    ]

    game.move_right()

    expected_board = [
        [2, 4, 8, 16],
        [0, 0, 4, 8],
        [0, 0, 2, 4],
        [0, 0, 16, 16],
    ]

    assert get_board_values(game.board) == expected_board

    assert game.score == (36, 16)


def test_move_right_complex_merge_var2(game):
    game.reset()
    game._board = [
        [Tile(2), Tile(2), Tile(4), Tile(4)],
        [Tile(4), Tile(4), Tile(8), Tile(8)],
        [Tile(16), Tile(16), Tile(32), Tile(0)],
        [Tile(0), Tile(0), Tile(0), Tile(0)],
    ]

    game.move_right()

    expected_board = [
        [0, 0, 4, 8],
        [0, 0, 8, 16],
        [0, 0, 32, 32],
        [0, 0, 0, 0],
    ]

    assert get_board_values(game.board) == expected_board

    assert game.score == (68, 32)


def test_move_right_empty_board(game):
    game.reset()
    # Initialize a board state with all zeros
    game._board = [
        [Tile(0), Tile(0), Tile(0), Tile(0)],
        [Tile(0), Tile(0), Tile(0), Tile(0)],
        [Tile(0), Tile(0), Tile(0), Tile(0)],
        [Tile(0), Tile(0), Tile(0), Tile(0)],
    ]

    game.move_right()

    expected_board = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]

    assert get_board_values(game.board) == expected_board

    assert game.score == (0, 0)


def test_move_right_no_move_possible(game):
    game.reset()
    # Initialize a board state with no possible moves
    game._board = [
        [Tile(2), Tile(4), Tile(2), Tile(4)],
        [Tile(4), Tile(2), Tile(4), Tile(2)],
        [Tile(2), Tile(4), Tile(2), Tile(4)],
        [Tile(4), Tile(2), Tile(4), Tile(2)],
    ]

    game.move_right()

    expected_board = [
        [2, 4, 2, 4],
        [4, 2, 4, 2],
        [2, 4, 2, 4],
        [4, 2, 4, 2],
    ]

    assert get_board_values(game.board) == expected_board

    assert game.score == (0, 0)
