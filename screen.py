from tkinter import *
from player import Player
from deck import Deck


class Game:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle_deck()
        self.root = Tk()

    def choice_hit(self, player1, player2, player1_values):
        player1.take_card(self.deck.pull_out_single_card())
        card_button1 = Button(self.root, text=player1.cards_in_hand[-1], width=7, height=4)
        player1.buttons.append(card_button1)
        card_button1.grid(row=6, column=len(player1.cards_in_hand))

        player2.take_card(self.deck.pull_out_single_card())
        card_button2 = Button(self.root, text="Card", width=7, height=4)
        player2.buttons.append(card_button2)
        card_button2.grid(row=2, column=len(player2.cards_in_hand))

        player1_values.config(text=f"Values card: {player1.values_cards_in_hand()}")

    @staticmethod
    def choice_pass(player1, player2, player2_values, winner_label):
        player2_values.config(text=f"Values card: {player2.values_cards_in_hand()}")
        for number, button in enumerate(player2.buttons):
            button.config(text=player2.cards_in_hand[number])
        if player1.values_cards_in_hand() <= player2.values_cards_in_hand() or player1.values_cards_in_hand() > 21:
            winner_label.config(text=f"The winner is {player2.name}")
        else:
            winner_label.config(text=f"The winner is {player1.name}")

    def play(self):
        self.root.geometry("400x400")
        player1 = Player("Patryk")
        player2 = Player("Croupier")
        player1_name = Label(self.root, text=player1.name, width=10)
        player1_name.grid(row=10, column=3)
        player2_name = Label(self.root, text=player2.name, width=10)
        player2_name.grid(row=0, column=3)

        for number in range(2):
            player1.take_card(self.deck.pull_out_single_card())
            card_button1 = Button(self.root, text=player1.cards_in_hand[number], width=7, height=4)
            player1.buttons.append(card_button1)
            card_button1.grid(row=6, column=number)

            player2.take_card(self.deck.pull_out_single_card())
            card_button2 = Button(self.root, text="Card", width=7, height=4)
            player2.buttons.append(card_button2)
            card_button2.grid(row=2, column=number)

        player1_values = Label(self.root, text=f"Values card: {player1.values_cards_in_hand()}", width=15)
        player1_values.grid(row=7, column=3)
        empty = Label(self.root, height=3)
        empty.grid(row=3, column=3)
        winner_laber = Label(self.root, text="", width=20)
        winner_laber.grid(row=4, column=3)
        empty2 = Label(self.root, height=3)
        empty2.grid(row=5, column=3)
        player2_values = Label(self.root, text=f"Values card: XXX", width=15)
        player2_values.grid(row=1, column=3)

        next_step = Label(self.root, text="What is your's next step?", width=20)
        next_step.grid(row=8, column=3)

        next_step_button2 = Button(self.root, text="HIT", width=8)
        next_step_button2.grid(row=9, column=2)
        next_step_button2.config(command=lambda: self.choice_hit(player1, player2, player1_values))

        next_step_button = Button(self.root, text="PASS", width=8)
        next_step_button.grid(row=9, column=4)
        next_step_button.config(command=lambda: self.choice_pass(player1, player2, player2_values, winner_laber))

        print(player1.buttons)
        self.root.mainloop()
        print(player1.buttons)


game = Game()
game.play()
