"""CLass Deck in BlackJack"""
from random import shuffle
from card import Card


class Deck:
    """Creation Deck with 52 cards"""
    def __init__(self):
        self.colors_cards = ["♥", "♦", "♠", "♣"]
        self.values_cards = [*range(2, 11)]
        self.values_cards.extend(["J", "Q", "K", "AS"])
        self.deck = [Card(value, color)
                     for value in self.values_cards
                     for color in self.colors_cards
                     ]

    def __str__(self):
        output = "Talia kart:\n"
        for letter in self.deck:
            output += f"{letter}\n"
        return output

    def shuffle_deck(self):
        """Function which shuffle all card in deck"""
        shuffle(self.deck)

    def pull_out_single_card(self):
        """Function which pull out single card from deck"""
        return self.deck.pop(0)
