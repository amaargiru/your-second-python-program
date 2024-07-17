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
