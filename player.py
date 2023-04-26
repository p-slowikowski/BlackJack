"""Class Player"""

class Player:
    """Class Player or Croupier"""
    def __init__(self, name):
        self.name = name
        self.cards_in_hand = []
        self.values = 0
        self.buttons = []

    def take_card(self, card):
        """Input card form deck and giving to player"""
        return self.cards_in_hand.append(card)

    def values_cards_in_hand(self):
        """Base game logic"""
        self.values = 0
        number_of_aces = len([card for card in self.cards_in_hand if card.value == "AS"])

        if number_of_aces == 2 and len(self.cards_in_hand) == 2:
            return 21

        if number_of_aces == 1 and len(self.cards_in_hand) == 2:
            self.values = 10

        for card in self.cards_in_hand:
            if card == "AS":
                self.values += 1
            elif card in ["Q", "J", "K"]:
                self.values += 10
            else:
                self.values += card.value

        return self.values

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.name}"

    def show_card(self):
        """Print all card in player hand"""
        output = ""
        for letter, card in enumerate(self.cards_in_hand):
            output += f"{card}\n"
        return output

    def remove_card_from_hand(self):
        """Remove card from hand when player want play again (tkinter version)"""
        self.cards_in_hand.clear()
        self.buttons.clear()
