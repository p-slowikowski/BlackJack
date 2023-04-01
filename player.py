

class Player:
    def __init__(self, name):
        self.name = name
        self.cards_in_hand = []

    def take_card(self, card):
        return self.cards_in_hand.append(card)

    def values_cards_in_hand(self):
        values = 0
        for card in self.cards_in_hand:
            values += card
        return values


class Human(Player):
    def __init__(self, name):
        super.__init__(name)
    pass


class Croupier(Player):
    def __init__(self, name):
        super.__init__(name)
    pass
