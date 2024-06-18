class Tile:
    """Плитка"""

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


class Score:
    """Текущий счёт"""

    def __init__(self, value: int):
        self._value: int = value
        """Величина текущего счёт"""
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


class Game:
    def __init__(self, rows: int, cols: int):
        self._board: list[list[Tile]] = [[Tile(0)] * rows for _ in range(cols)]
        """Игровое поле"""
        self._score: Score = Score(0)
        self._is_game_over: bool = False


game = Game(4, 4)
