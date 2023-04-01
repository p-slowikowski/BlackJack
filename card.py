
class Card:
    def __init__(self, value, color):
        self.color = color
        self.value = value

    def __str__(self):
        return f"Card: {self.value}{self.color}"
