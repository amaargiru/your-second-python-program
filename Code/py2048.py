from Core.game import Game
from CLI.cli import Cli

game = Game(rows=4, columns=4)
game.reset()
game.add_random_tile()  # Add two tiles to the game board
game.add_random_tile()

Cli.pretty_print_board(game.board)
Cli.pretty_print_score(game.score)

game.move_up()

Cli.pretty_print_board(game.board)
Cli.pretty_print_score(game.score)
