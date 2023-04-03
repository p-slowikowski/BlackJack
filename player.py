

class Player:
    def __init__(self, name):
        self.name = name
        self.cards_in_hand = []
        self.values = 0

    def take_card(self, card):
        return self.cards_in_hand.append(card)

    def values_cards_in_hand(self):
        self.values = 0
        for card in self.cards_in_hand:
            if card == "Q" or card == "J" or card == "K" or card == "AS":
                self.values += 10
            else:
                self.values += card.value
        return f"Total values your cards: {self.values}"


class Human(Player):
    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return f"Hello. I'm {self.name} i to moje karty{self.cards_in_hand}"

    def show_card(self):
        output = ""
        for letter, card in enumerate(self.cards_in_hand):
            output += f"{card}\n"
        return output


class Croupier(Player):
    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return f"Hello. I'm {self.name}"
