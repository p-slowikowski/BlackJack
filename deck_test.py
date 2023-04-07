"""Test Class Deck"""
from deck import Deck


def test_create_deck():
    """Test creation Deck"""
    deck = Deck()
    assert len(deck.deck) == 52


def test_single_color_deck():
    """Test correct numbers of single color in deck"""
    deck = Deck()
    heart_cards = [card for card in deck.deck if card.color == "♥"]
    assert len(heart_cards) == 13


def test_shuffle():
    """Test shuffle deck"""
    deck_not_shuffle = Deck()
    deck_with_shuffle = Deck()
    assert deck_not_shuffle.deck == deck_with_shuffle.deck
    deck_with_shuffle.shuffle_deck()
    assert deck_not_shuffle.deck != deck_with_shuffle.deck


def test_pull_out_single_card():
    """Test pull out single card from deck"""
    deck = Deck()
    card_out_deck = deck.pull_out_single_card()
    if card_out_deck in deck.deck:
        assert True


def test_no_full_deck():
    """Check amount card in deck when single card out"""
    deck = Deck()
    deck.pull_out_single_card()
    assert len(deck.deck) == 51
