class InvalidColor(Exception):
    pass


class InvalidValue(Exception):
    pass


class Card:

    POSSIBLE_VALUES = list(range(2, 11)) + ["J", "Q", "K", "AS"]
    POSSIBLE_COLORS = ["♥", "♦", "♠", "♣"]

    def __init__(self, value, color):
        if color in Card.POSSIBLE_COLORS:
            self.color = color
        else:
            raise InvalidColor("Invalid card color!")
        if value in Card.POSSIBLE_VALUES:
            self.value = value
        else:
            raise InvalidValue("Invalid card value!")

    def __str__(self):
        return f"Card: {self.value}{self.color}"

    def __repr__(self):
        return f"{self.value} -> {self.color}"

    def __eq__(self, other):
        return self.value == other
