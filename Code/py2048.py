import os

from pynput import keyboard
from pynput.keyboard import Key

from CLI.cli import Cli
from Core.game import Game

game = Game(rows=4, columns=4)
game.reset()
game.add_random_tile()
game.add_random_tile()

Cli.pretty_print_board(game.board)
Cli.pretty_print_score(game.score)


def on_key_press(key):
    if key == Key.left:
        game.move_left()
    elif key == Key.right:
        game.move_right()
    elif key == Key.up:
        game.move_up()
    elif key == Key.down:
        game.move_down()
    elif key == Key.esc:
        exit(0)

    if key in [Key.left, Key.right, Key.up, Key.down]:
        os.system('cls' if os.name == 'nt' else 'clear')
        game.add_random_tile()
        Cli.pretty_print_board(game.board)
        Cli.pretty_print_score(game.score)


with keyboard.Listener(on_press=on_key_press) as listener:
    listener.join()
