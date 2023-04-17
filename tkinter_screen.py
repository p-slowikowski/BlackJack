from tkinter import *
from player import Player
from deck import Deck


class Game:
    def __init__(self):
        self.root = Tk()
        self.name_player = None
        self.list_players = []
        self.deck = Deck()

    def window(self):
        self.root.geometry("1000x1000")
        self.root.resizable(width=False, height=False)
        self.root.title("BlackJack")
        self.main_menu()
        self.root.mainloop()

    def choice_hit(self, player1, player2, player1_values, game):
        player1.take_card(self.deck.pull_out_single_card())
        card_button1 = Button(game, text=player1.cards_in_hand[-1], width=7, height=4)
        player1.buttons.append(card_button1)
        card_button1.grid(row=6, column=len(player1.cards_in_hand))

        player2.take_card(self.deck.pull_out_single_card())
        card_button2 = Button(game, text="Card", width=7, height=4)
        player2.buttons.append(card_button2)
        card_button2.grid(row=2, column=len(player2.cards_in_hand))

        player1_values.config(text=f"Values card: {player1.values_cards_in_hand()}")

    def choice_pass(self, player1, player2, player2_values, winner_label, game):
        player2_values.config(text=f"Values card: {player2.values_cards_in_hand()}")
        for number, button in enumerate(player2.buttons):
            button.config(text=player2.cards_in_hand[number])
        if player1.values_cards_in_hand() <= player2.values_cards_in_hand() or player1.values_cards_in_hand() > 21:
            winner_label.config(text=f"The winner is {player2.name}")
        else:
            winner_label.config(text=f"The winner is {player1.name}")
        play_again_button = Button(game, text="Play Again", command=lambda: [self.reload_game(game)])
        play_again_button.grid(row=5, column=0)
        play_again_button = Button(game, text="Exit", command=lambda: self.root.quit())
        play_again_button.grid(row=5, column=1)

    def reload_game(self, game):
        game.grid_forget()
        self.first_game()

    def first_game(self):
        game = Frame(self.root)
        game.grid(row=0, column=0)
        if len(self.deck.deck) > 5:
            player1 = self.list_players[0]
            player2 = self.list_players[1]

            player1_name = Label(game, text=self.list_players[0], width=50)
            player1_name.grid(row=10, column=1)

            player2_name = Label(game, text=self.list_players[1], width=50)
            player2_name.grid(row=0, column=1)

            for number in range(2):
                player1.take_card(self.deck.pull_out_single_card())
                card_button1 = Button(game, text=player1.cards_in_hand[number], width=7, height=4)
                player1.buttons.append(card_button1)
                card_button1.grid(row=6, column=number)

                player2.take_card(self.deck.pull_out_single_card())
                card_button2 = Button(game, text="Card", width=7, height=4)
                player2.buttons.append(card_button2)
                card_button2.grid(row=2, column=number)

            player1_values = Label(game, text=f"Values card: {player1.values_cards_in_hand()}")
            player1_values.grid(row=7, column=0)
            player2_values = Label(game, text=f"Values card: XXX", width=15)
            player2_values.grid(row=1, column=0)

            next_step = Label(game, text="What is your's next step?", width=20)
            next_step.grid(row=8, column=0)

            next_step_button2 = Button(game, text="HIT", width=8)
            next_step_button2.grid(row=9, column=0)
            next_step_button2.config(command=lambda: self.choice_hit(player1, player2, player1_values, game))

            winner_label = Label(game, text="")
            winner_label.grid(row=4, column=0)

            next_step_button = Button(game, text="PASS", width=8)
            next_step_button.grid(row=9, column=1)
            next_step_button.config(command=lambda: self.choice_pass(player1, player2, player2_values,
                                                                     winner_label, game))
        else:
            game.grid_forget()
            game_over_label = Label(self.root, text="Deck has been empted")
            game_over_label.grid(row=0, column=0)
            exit_button = Button(self.root, text="Exit", command=lambda: self.root.quit())
            exit_button.grid(row=1, column=0)

    def main_menu(self):
        self.root.update()
        menu = Frame(self.root)
        menu.grid(row=0, column=0)

        name_label = Label(menu, text="Enter your's name and press PLAY", width=50)
        name_label.grid(row=0, column=0)

        input_name = Entry(menu)
        input_name.grid(row=1, column=0)

        button_play = Button(menu, text="PLAY", width=8)
        button_play.grid(row=2, column=0)
        button_play.config(command=lambda: [self.save_name(input_name),
                                            self.menu_grid_forget(menu),
                                            self.initialize_game(),
                                            self.first_game()])

        button_exit = Button(menu, text="EXIT", width=8)
        button_exit.grid(row=3, column=0)
        button_exit.config(command=lambda: self.root.quit())

    def save_name(self, input_name):
        self.name_player = input_name.get()

    @staticmethod
    def menu_grid_forget(menu):
        menu.grid_forget()

    def initialize_game(self):
        player1 = Player(self.name_player)
        self.list_players.append(player1)
        croupier = Player("Croupier")
        self.list_players.append(croupier)


game = Game()
game.window()
