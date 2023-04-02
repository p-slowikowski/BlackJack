from card import Card
from random import shuffle


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

    def shuffle_deck(self):
        shuffle(self.deck)

    def pull_out_single_card(self):
        return self.deck.pop(0)
