

class Player:
    def __init__(self, name):
        self.name = name
        self.cards_in_hand = []
        self.values = 0

    def take_card(self, card):
        return self.cards_in_hand.append(card)

    def values_cards_in_hand(self):
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

        return f"Total values your cards: {self.values}"

    def __str__(self):
        return f"Hello. I'm {self.name} i to moje karty{self.cards_in_hand}"

    def show_card(self):
        output = ""
        for letter, card in enumerate(self.cards_in_hand):
            output += f"{card}\n"
        return output
