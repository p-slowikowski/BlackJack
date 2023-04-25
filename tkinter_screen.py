"""visualize in tkinter window BlackJack game"""
from tkinter import *
from player import Player
from deck import Deck


class Game:
    """Main class Game"""
    def __init__(self):
        self.root = Tk()
        self.name_player = None
        self.list_players = []
        self.deck = Deck()
        self.deck.shuffle_deck()

    def window(self):
        """
        Initialize main window
        """
        self.root.geometry("600x400")
        self.root.resizable(width=False, height=False)
        self.root.title("BlackJack")
        self.main_menu()
        self.root.mainloop()

    def choice_hit(self, player1, player2, player1_values, game):
        """
        After click button "HIT"
        Add user card and croupier, and show values cards in hand
        """
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
        """
        After click button "Pass"
        Check which player won and show buttons: "Play again" and "Exit"
        """
        player2_values.config(text=f"Values card: {player2.values_cards_in_hand()}")
        for number, button in enumerate(player2.buttons):
            button.config(text=player2.cards_in_hand[number])
        if player1.values_cards_in_hand() <= player2.values_cards_in_hand()\
                or player1.values_cards_in_hand() > 21:
            winner_label.config(text=f"The winner is {player2.name}")
        else:
            winner_label.config(text=f"The winner is {player1.name}")
        play_again_button = Button(game, text="Play Again", command=lambda: [self.reload_game(game)])
        play_again_button.grid(row=5, column=8)
        play_again_button = Button(game, width=8, text="Exit", command=lambda: self.root.quit())
        play_again_button.grid(row=5, column=9)

    def reload_game(self, game):
        """
        Reload window when user want play again
        """
        game.grid_forget()
        self.first_game()

    def first_game(self):
        """
        Initialize first game
        """
        game = Frame(self.root)
        game.grid(row=0, column=0)
        if len(self.deck.deck) > 5:
            player1 = self.list_players[0]
            player2 = self.list_players[1]

            player1_name = Label(game, text=self.list_players[0])
            player1_name.grid(row=10, column=7)

            player2_name = Label(game, text=self.list_players[1])
            player2_name.grid(row=0, column=7)

            if len(player1.cards_in_hand) > 1:
                player1.remove_card_from_hand()
                player2.remove_card_from_hand()

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
            player1_values.grid(row=7, column=7)
            player2_values = Label(game, text=f"Values card: XXX")
            player2_values.grid(row=1, column=7)

            next_step = Label(game, text="What is your's next step?")
            next_step.grid(row=8, column=7)

            next_step_button2 = Button(game, text="HIT", width=8)
            next_step_button2.grid(row=8, column=8)
            next_step_button2.config(command=lambda: self.choice_hit(player1, player2,
                                                                     player1_values, game))

            winner_label = Label(game, text="")
            winner_label.grid(row=4, column=7)

            next_step_button = Button(game, text="PASS", width=8)
            next_step_button.grid(row=8, column=9)
            next_step_button.config(command=lambda: self.choice_pass(player1, player2, player2_values,
                                                                     winner_label, game))
        else:
            game.grid_forget()
            game_over_label = Label(self.root, text="Deck has been empted")
            game_over_label.grid(row=0, column=0)
            exit_button = Button(self.root, text="Exit", command=lambda: self.root.quit())
            exit_button.grid(row=1, column=0)

    def main_menu(self):
        """
        Show main_manu, user can enter his name and play
        """
        self.root.update()
        menu = Frame(self.root)
        menu.grid(row=0, column=0)

        name_label = Label(menu, text="Enter your's name and press PLAY", width=50)
        name_label.grid(row=0, column=7)

        input_name = Entry(menu)
        input_name.grid(row=1, column=7)

        button_play = Button(menu, text="PLAY", width=8)
        button_play.grid(row=2, column=7)
        button_play.config(command=lambda: [self.save_name(input_name),
                                            self.menu_grid_forget(menu),
                                            self.initialize_game(),
                                            self.first_game()])

        button_exit = Button(menu, text="EXIT", width=8)
        button_exit.grid(row=3, column=7)
        button_exit.config(command=lambda: self.root.quit())

    def save_name(self, input_name):
        """
        Save user's name in class Game
        """
        self.name_player = input_name.get()

    @staticmethod
    def menu_grid_forget(menu):
        """
        Clear mian menu when user entered his name
        """
        menu.grid_forget()

    def initialize_game(self):
        """
        Create Player and Croupier object and append to list of players
        """
        player1 = Player(self.name_player)
        self.list_players.append(player1)
        croupier = Player("Croupier")
        self.list_players.append(croupier)


game = Game()
game.window()
