from player import Player
from deck import Deck


class Game:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle_deck()

    def play(self):
        player1 = Player("Patryk")
        player2 = Player("Croupier")
        for _ in range(0, 2):
            player1_card = player1.take_card(self.deck.pull_out_single_card())
            player2_card = player2.take_card(self.deck.pull_out_single_card())
        print(player1.show_card())
        print(player1.values_cards_in_hand())

        while True:
            user_choice = input(print("Dobierasz czy pasujesz? (D czy P wciśnij"))
            if user_choice == "D":
                player1_card_3 = player1.take_card(self.deck.pull_out_single_card())
                player2_card_3 = player2.take_card(self.deck.pull_out_single_card())
                print(player1.show_card())
                print(player1.values_cards_in_hand())
            elif user_choice == "D":
                break
            else:
                print("Dokonano nieprawidłowego wyboru!")
            




# if len(player1.cards_in_hand) <= 2 and player1.values >= 20:
#     print(f"Gracz {player1.name} wygrał!")
#     exit()


# while True:
#     user_choice = input(print("Dobierasz czy pasujesz? (D czy P wciśnij"))
#     if user_choice == "D":
#         player_card = croupier.take_card(deck.pull_out_single_card())
#         croupier_card = player1.take_card(deck.pull_out_single_card())
#
#     elif user_choice == "P":
#         if croupier.values > player1.values and player1.values < 21:
#             print(f'"krupier wygrał')
#         else:
#             print(f"Gracz wygrał")
#
#     print(player1.show_card())
#     print(player1.values_cards_in_hand())
