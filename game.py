import player
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
        if player1.values_cards_in_hand() == 21:
            print(f"Wygrał: {player1.name}")
            exit()

        while True:
            user_choice = input(print("Dobierasz czy pasujesz? (D czy P wciśnij"))
            if user_choice == "D":
                player1_nextcard = player1.take_card(self.deck.pull_out_single_card())
                player2_nextcard = player2.take_card(self.deck.pull_out_single_card())
                print(player1.show_card())
                print(player1.values_cards_in_hand())
            elif user_choice == "P":
                break
            else:
                print("Dokonano nieprawidłowego wyboru!")

        if player1.values_cards_in_hand() <= player2.values_cards_in_hand() or player1.values_cards_in_hand() > 21:
            print(f"Karty {player1.name}: {player1.show_card()}. Wartość: {player1.values_cards_in_hand()} ")
            print(f"Karty {player2.name}: {player2.show_card()}. Wartość: {player2.values_cards_in_hand()} ")
            print(f"Wygrał {player2.name}")
        else:
            print(f"Karty {player1.name}: {player1.show_card()}. Wartość: {player1.values_cards_in_hand()} ")
            print(f"Karty {player2.name}: {player2.show_card()}. Wartość: {player2.values_cards_in_hand()} ")
            print(f"Wygrał {player1.name}")
