from colorama import Style, Fore

from CLI.cli import Cli
from Core.tile import Tile


def test_pretty_print_board(capsys):
    board = [[Tile(0), Tile(2), Tile(4), Tile(8)],
             [Tile(16), Tile(32), Tile(64), Tile(128)],
             [Tile(256), Tile(512), Tile(1024), Tile(2048)],
             [Tile(4096), Tile(8192), Tile(16384), Tile(32768)]]

    Cli.pretty_print_board(board)
    captured = capsys.readouterr()
    assert "+-------+-------+-------+-------+" in captured.out
    assert "|   0   |" in captured.out
    assert Style.RESET_ALL in captured.out
    assert Fore.RED in captured.out


def test_pretty_print_score(capsys):
    Cli.pretty_print_score((1024, 34))
    captured = capsys.readouterr()
    assert "Score: 1024" in captured.out
    assert Fore.RED in captured.out
    assert "+34" in captured.out
    assert Style.RESET_ALL in captured.out


def test_is_power_of_two():
    assert Cli._is_power_of_two(1) is True
    assert Cli._is_power_of_two(2) is True
    assert Cli._is_power_of_two(3) is False
    assert Cli._is_power_of_two(4) is True
    assert Cli._is_power_of_two(0) is False


def test_get_color_for_power_of_two():
    assert Cli._get_color_for_power_of_two(2) == Fore.RED
    assert Cli._get_color_for_power_of_two(4) == Fore.GREEN
    assert Cli._get_color_for_power_of_two(8) == Fore.YELLOW
    assert Cli._get_color_for_power_of_two(1024) == Fore.GREEN


def test_get_color_of_score_diff():
    assert Cli._get_color_of_score_diff(10) == Fore.BLACK
    assert Cli._get_color_of_score_diff(30) == Fore.GREEN
    assert Cli._get_color_of_score_diff(50) == Fore.RED
