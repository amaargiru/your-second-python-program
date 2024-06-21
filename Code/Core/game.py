import random


class Score:
    """Текущий счёт"""

    def __init__(self, value: int):
        self._value: int = value
        """Величина текущего счёта"""
        self._diff: int = 0
        """Скорость изменения счёта"""
        # Может быть полезна при индикации счёта. Высокая скорость изменения -> удачный ход -> поздравление красным цветом

    @property
    def value(self) -> int:
        return self._value

    @value.setter
    def value(self, value):
        if value < 0:
            raise ValueError("The value of the scored points must be not less than zero.")
        if value % 2 != 0:
            raise ValueError("The value of the scored points must be an even number.")
        if value < self._value:
            raise ValueError("The value of the scored points should not decrease.")

        self._diff = value - self._value
        self._value = value

    @property
    def diff(self) -> int:
        return self._diff


class Tile:
    """Одиночная плитка"""

    # Плитка выделена в отдельный класс для возможности дальнейшего расширения. Например, в консольной игре к ней можно
    # добавить свойство "Цвет", в режиме обучения можно выделять одинаковые плитки, расположенные рядом и т. д.

    def __init__(self, value: int):
        self.value: int = value  # Call value setter
        """Номинал плитки"""

    @property
    def value(self) -> int:
        return self._value

    @value.setter
    def value(self, value):
        if value < 0:
            raise ValueError("The value of the tile must be not less than zero.")
        if value % 2 != 0:
            raise ValueError("The value of the tile must be an even number.")

        self._value = value


class Game:
    def __init__(self, rows: int, cols: int):
        self._rows = rows
        self._cols = cols

        self._board: list[list[Tile]] = []
        """Game board"""
        self._score: Score = Score(0)
        """Game Score"""
        self._is_game_over: bool = False
        """Признак невозможности дальнейших ходов"""

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
        """Инициализация перед началом игры"""
        self._score.value = 0
        self._score.value = 0  # Повторный ноль обнуляет скорость роста счёта
        self._is_game_over = False
        self._board = [[Tile(0)] * self._rows for _ in range(self._cols)]

        self._add_random_tile()  # Добавляем на игровое поле две плитки
        self._add_random_tile()

    def move_left(self) -> None:
        pass

    def move_right(self) -> None:
        pass

    def move_up(self) -> None:
        pass

    def move_down(self) -> None:
        pass

    def _add_random_tile(self) -> bool:
        """Add new tile to the board, if possible"""
        zero_tiles = [(i, j) for i in range(len(self._board)) for j in range(len(self._board[0])) if self._board[i][j] == 0]

        if not zero_tiles:
            return False  # No zero places in the board

        i, j = random.choice(zero_tiles)
        # The new tile must be 2 with 90% probability or 4 with 10% probability
        self._board[i][j].value = random.choices([2, 4], [0.9, 0.1])[0]

        return True

    def _is_move_possible(self):
        for row in range(self._rows):
            for col in range(self._cols):
                if (self._board[row][col].value == 0
                        or row > 0 and self.board[row][col].value == self.board[row - 1][col].value
                        or col > 0 and self.board[row][col].value == self.board[row][col - 1].value):
                    return True
        return False
