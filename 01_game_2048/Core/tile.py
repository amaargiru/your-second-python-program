class Tile:
    """Single tile"""

    # The tile is separated into a distinct class to allow for further extension. For example, in a console game, it can have a "Color"
    # property added, in a learning mode, identical tiles located next to each other can be visually highlighted, etc.

    def __init__(self, value: int):
        self.value: int = value  # Call value setter with validation
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
