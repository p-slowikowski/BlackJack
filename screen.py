import tkinter
from tkinter import Tk, Button, Label
from player import Player
from deck import Deck


class Game:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle_deck()

    @staticmethod
    def click_action(button, card):
        button.config(text=card)

    def play(self):
        root = Tk()
        root.geometry("400x400")
        player1 = Player("Patryk")
        player2 = Player("Croupier")
        for _ in range(0, 2):
            player1_card = player1.take_card(self.deck.pull_out_single_card())
            player2_card = player2.take_card(self.deck.pull_out_single_card())

        card_button1 = Button(root, text="Card", width=8)
        card_button1.pack(side=tkinter.BOTTOM)
        card_button1.config(command=lambda: self.click_action(card_button1, player1.cards_in_hand[0]))
        card_button2 = Button(root, text="Card", width=8)
        card_button2.pack(side=tkinter.BOTTOM)
        card_button2.config(command=lambda: self.click_action(card_button2, player1.cards_in_hand[1]))

        card_button3 = Button(root, text="Card", width=8)
        card_button3.pack(side=tkinter.TOP)
        # card_button3.config(command=lambda: self.click_action(card_button3, player2.cards_in_hand[0]))
        card_button4 = Button(root, text="Card", width=8)
        card_button4.pack(side=tkinter.TOP)
        # card_button4.config(command=lambda: self.click_action(card_button4, player2.cards_in_hand[1]))

        player1_name = Label(root, text=player1.name, width=10)
        player1_name.pack(side=tkinter.BOTTOM)
        player2_name = Label(root, text=player2.name, width=10)
        player2_name.pack(side=tkinter.TOP)

        player1_values = Label(root, text=player1.values_cards_in_hand(), width=10)
        player1_values.pack(side=tkinter.BOTTOM)
        root.mainloop()


game = Game()
game.play()
