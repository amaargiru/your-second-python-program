import random


class Score:
    """Current score"""

    def __init__(self, value: int):
        self._value: int = value
        """The value of the current score"""
        self._diff: int = value
        """Score change speed"""
        # Knowledge of the score change speed can be useful when displaying the score to the player.
        # For example, high change speed -> successful move -> congratulations with red color

    @property
    def value(self) -> int:
        return self._value

    @value.setter
    def value(self, value):
        self.validate_value(value)

        self._diff = value - self._value
        self._value = value

    def validate_value(self, value):
        if value < 0:
            raise ValueError("The value of the scored points must be not less than zero.")
        if value % 2 != 0:
            raise ValueError("The value of the scored points must be an even number.")
        if value < self._value:
            raise ValueError("The value of the scored points should not decrease.")

    @property
    def diff(self) -> int:
        return self._diff


class Tile:
    """Single tile"""

    # The tile is separated into a distinct class to allow for further extension. For example, in a console game, it can have a "Color"
    # property added, in a learning mode, identical tiles located next to each other can be visually highlighted, etc.

    def __init__(self, value: int):
        self.value: int = value  # Call value setter
        """The value of the current tile"""

    @property
    def value(self) -> int:
        return self._value

    @value.setter
    def value(self, value):
        self.validate_value(value)

        self._value = value

    @classmethod
    def validate_value(cls, value):
        if value < 0:
            raise ValueError("The value of the tile must be not less than zero.")
        if value % 2 != 0:
            raise ValueError("The value of the tile must be an even number.")


class Game:
    def __init__(self, rows: int, columns: int):
        self._rows = rows
        self._columns = columns

        self._board: list[list[Tile]] = []
        """Game board"""
        self._score: Score = Score(0)
        """Game Score"""
        self._is_game_over: bool = False
        """Indication of no further possible moves"""

    @property
    def board(self) -> list[list[Tile]]:
        return self._board

    @property
    def score(self) -> tuple[int, int]:
        return self._score.value, self._score.diff

    @property
    def is_game_over(self) -> bool:
        return self._is_game_over

    def reset(self) -> None:
        """Initialization before the start of the game"""
        self._score.value = 0
        self._score.value = 0  # Resetting to zero again resets the score change speed
        self._is_game_over = False
        self._board = [[Tile(0) for _ in range(self._columns)] for _ in range(self._rows)]

        self._add_random_tile()  # Add two tiles to the game board
        self._add_random_tile()

    def move_left(self) -> None:
        for row in range(len(self._board)):
            extra_tiles: int = 0

            new_row = [i for i in self._board[row] if i.value != 0]
            if len(new_row) >= 2:
                for i in range(len(new_row) - 1):
                    if new_row[i].value == new_row[i + 1].value:
                        new_row[i].value *= 2
                        new_row[i + 1].value = 0
                        self._score.value += new_row[i].value
                        extra_tiles += 1
            self._board[row] = [i for i in new_row if i.value != 0] + [Tile(0)] * (self._columns - len(new_row) + extra_tiles)

    def move_right(self) -> None:
        for row in range(len(self._board)):
            extra_tiles: int = 0

            new_row = [i for i in self._board[row] if i.value != 0]
            if len(new_row) >= 2:
                for i in range(len(new_row) - 1, 0, -1):
                    if new_row[i].value == new_row[i - 1].value:
                        new_row[i].value *= 2
                        new_row[i - 1].value = 0
                        self._score.value += new_row[i].value
                        extra_tiles += 1
            self._board[row] = [Tile(0)] * (self._columns - len(new_row) + extra_tiles) + [i for i in new_row if i.value != 0]

    def move_up(self) -> None:
        for col in range(self._columns):
            extra_tiles: int = 0

            new_col = [self._board[row][col] for row in range(len(self._board)) if self._board[row][col].value != 0]
            if len(new_col) >= 2:
                for i in range(len(new_col) - 1):
                    if new_col[i].value == new_col[i + 1].value:
                        new_col[i].value *= 2
                        new_col[i + 1].value = 0
                        self._score.value += new_col[i].value
                        extra_tiles += 1

            merged_col = [i for i in new_col if i.value != 0] + [Tile(0)] * (len(self._board) - len(new_col) + extra_tiles)

            for row in range(len(self._board)):
                self._board[row][col] = merged_col[row]

    def move_down(self) -> None:
        for col in range(self._columns):
            extra_tiles: int = 0

            new_col = [self._board[row][col] for row in range(len(self._board)) if self._board[row][col].value != 0]
            if len(new_col) >= 2:
                for i in range(len(new_col) - 1, 0, -1):
                    if new_col[i].value == new_col[i - 1].value:
                        new_col[i].value *= 2
                        new_col[i - 1].value = 0
                        self._score.value += new_col[i].value
                        extra_tiles += 1

            merged_col = [Tile(0)] * (len(self._board) - len(new_col) + extra_tiles) + [i for i in new_col if i.value != 0]

            for row in range(len(self._board)):
                self._board[row][col] = merged_col[row]

    def _add_random_tile(self) -> bool:
        """Add new tile to the board, if possible"""
        zero_tiles: list[tuple] = [(i, j) for i in range(len(self._board))
                                   for j in range(len(self._board[0]))
                                   if self._board[i][j].value == 0]

        if not zero_tiles:
            return False  # No zero places in the board

        i, j = random.choice(zero_tiles)
        # The new tile must be 2 with 90% probability or 4 with 10% probability
        self._board[i][j].value = random.choices([2, 4], [0.9, 0.1])[0]

        return True

    def _is_move_possible(self):
        for row in range(self._rows):
            for col in range(self._columns):
                if (self._board[row][col].value == 0
                        or row > 0 and self._board[row][col].value == self._board[row - 1][col].value
                        or col > 0 and self._board[row][col].value == self._board[row][col - 1].value):
                    return True
        return False
