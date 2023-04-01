from card import Card


class Deck:
    def __init__(self):
        self.colors_cards = ["♥", "♦", "♠", "♣"]
        self.values_cards = [*range(2, 11)]
        self.values_cards.extend(["J", "Q", "K", "AS"])
        self.deck = [Card(value, color) for value in self.values_cards for color in self.colors_cards]

    def __str__(self):
        output = "Talia kart:\n"
        for letter in self.deck:
            output += f"{letter}\n"
        return output

