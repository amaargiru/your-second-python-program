from Core.game import Game
from terminal import Terminal

game = Game(rows=3, columns=5)
game.reset()

Terminal.pretty_print_2d_list(game.board)
game.move_down()
game.add_random_tile()  # Add two tiles to the game board
game.add_random_tile()
Terminal.pretty_print_2d_list(game.board)