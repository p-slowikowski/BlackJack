from tkinter import *
from player import Player
from deck import Deck


class Game:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle_deck()
        self.root = Tk()
        self.menu = Frame(self.root)
        self.game = Frame(self.root)
        self.frame_player1 = Frame(self.game)
        self.frame_player2 = Frame(self.game)

    def choice_hit(self, player1, player2, player1_values):
        player1.take_card(self.deck.pull_out_single_card())
        card_button1 = Button(self.frame_player1, text=player1.cards_in_hand[-1], width=7, height=4)
        player1.buttons.append(card_button1)
        card_button1.grid(row=0, column=len(player1.cards_in_hand))

        player2.take_card(self.deck.pull_out_single_card())
        card_button2 = Button(self.frame_player2, text="Card", width=7, height=4)
        player2.buttons.append(card_button2)
        card_button2.grid(row=0, column=len(player2.cards_in_hand))

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

    def let_game(self, input_name):
        name = input_name.get()
        self.menu.destroy()
        player1 = Player(name)
        player2 = Player("Croupier")
        self.game.grid(row=5, column=7)

        player1_name = Label(self.game, text=player1.name, width=10)
        player1_name.grid(row=10, column=3)

        player2_name = Label(self.game, text=player2.name, width=10)
        player2_name.grid(row=0, column=3)

        self.frame_player1.grid(row=6)
        self.frame_player2.grid(row=2)

        for number in range(2):
            player1.take_card(self.deck.pull_out_single_card())
            card_button1 = Button(self.frame_player1, text=player1.cards_in_hand[number], width=7, height=4)
            player1.buttons.append(card_button1)
            card_button1.grid(row=0, column=number)

            player2.take_card(self.deck.pull_out_single_card())
            card_button2 = Button(self.frame_player2, text="Card", width=7, height=4)
            player2.buttons.append(card_button2)
            card_button2.grid(row=0, column=number)

        player1_values = Label(self.game, text=f"Values card: {player1.values_cards_in_hand()}", width=15)
        player1_values.grid(row=7, column=3)
        empty = Label(self.game, height=3)
        empty.grid(row=3, column=3)
        winner_laber = Label(self.game, text="", width=20)
        winner_laber.grid(row=4, column=3)
        empty2 = Label(self.game, height=3)
        empty2.grid(row=5, column=3)
        player2_values = Label(self.game, text=f"Values card: XXX", width=15)
        player2_values.grid(row=1, column=3)

        next_step = Label(self.game, text="What is your's next step?", width=20)
        next_step.grid(row=8, column=3)

        choice_step = Frame(self.game)
        choice_step.grid(row=9, column=3)
        next_step_button2 = Button(choice_step, text="HIT", width=8)
        next_step_button2.grid(row=0, column=0)
        next_step_button2.config(command=lambda: self.choice_hit(player1, player2, player1_values))

        next_step_button = Button(choice_step, text="PASS", width=8)
        next_step_button.grid(row=0, column=1)
        next_step_button.config(command=lambda: self.choice_pass(player1, player2, player2_values, winner_laber))

        self.root.mainloop()

    def main_menu(self):
        self.root.geometry("400x400")
        self.root.resizable(width=False, height=False)
        self.root.title("BlackJack")
        self.menu.grid(row=0, column=0)

        name_label = Label(self.menu, text="Enter your's name and press PLAY", width=50)
        name_label.grid(row=0, column=0)

        input_name = Entry(self.menu)
        input_name.grid(row=1, column=0)

        button_play = Button(self.menu, text="PLAY", width=8)
        button_play.grid(row=2, column=0)
        button_play.config(command=lambda: self.let_game(input_name))

        button_exit = Button(self.menu, text="EXIT", width=8)
        button_exit.grid(row=3, column=0)
        button_exit.config(command=lambda: self.root.quit())
        self.root.mainloop()


game = Game()
game.main_menu()
