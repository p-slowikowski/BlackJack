from player import Player
from card import Card


def test_value_card_in_hand():
    card = Card(5, "♥")
    card2 = Card(7, "♥")
    player = Player("Patryk")
    player.take_card(card)
    player.take_card(card2)
    assert player.values_cards_in_hand() == 'Total values your cards: 12'


def test_values_two_aces_in_hand():
    card = Card("AS", "♥")
    card2 = Card("AS", "♥")
    player = Player("Patryk")
    player.take_card(card)
    player.take_card(card2)
    assert player.values_cards_in_hand() == 21


def test_values_ace_number_in_hand():
    card = Card("AS", "♥")
    card2 = Card(2, "♥")
    player = Player("Patryk")
    player.take_card(card)
    player.take_card(card2)
    assert player.values_cards_in_hand() == 'Total values your cards: 13'


def test_values_three_aces_in_hand():
    card = Card("AS", "♥")
    card2 = Card("AS", "♥")
    card3 = Card("AS", "♥")
    player = Player("Patryk")
    player.take_card(card)
    player.take_card(card2)
    player.take_card(card3)
    assert player.values_cards_in_hand() == 'Total values your cards: 3'

def test_values_two_kings_in_hand():
    card = Card("K", "♥")
    card2 = Card("K", "♥")
    player = Player("Patryk")
    player.take_card(card)
    player.take_card(card2)
    assert player.values_cards_in_hand() == 'Total values your cards: 20'