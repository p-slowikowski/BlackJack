from player import Human, Croupier
from deck import Deck

#
# class Game:
#     def __init__(self):
#         pass


player1 = Human("Patryk")
croupier = Croupier("Croupier")
deck = Deck()
deck.shuffle_deck()

for _ in range(0, 2):
    player_card = croupier.take_card(deck.pull_out_single_card())
    croupier_card = player1.take_card(deck.pull_out_single_card())
print(player1.show_card())
print(player1.values_cards_in_hand())
