from player import Human, Croupier
from deck import Deck


player1 = Human("Patryk")
croupier = Croupier("Croupier")
deck = Deck()
deck.shuffle_deck()

for _ in range(0, 2):
    player_card = croupier.take_card(deck.pull_out_single_card())
    croupier_card = player1.take_card(deck.pull_out_single_card())
print(player1.show_card())
print(player1.values_cards_in_hand())

if len(player1.cards_in_hand) <= 2 and player1.values >= 20:
    print(f"Gracz {player1.name} wygrał!")
    exit()


while True:
    user_choice = input(print("Dobierasz czy pasujesz? (D czy P wciśnij"))
    if user_choice == "D":
        player_card = croupier.take_card(deck.pull_out_single_card())
        croupier_card = player1.take_card(deck.pull_out_single_card())

    elif user_choice == "P":
        if croupier.values > player1.values and player1.values < 21:
            print(f'"krupier wygrał')
        else:
            print(f"Gracz wygrał")

    print(player1.show_card())
    print(player1.values_cards_in_hand())
