"""Unit test card.py files"""
from card import Card, InvalidValue, InvalidColor
import pytest


def test_creation():
    """Check creation card"""
    card = Card(10, "♥")
    assert card.color == "♥"
    assert card.value == 10


def test_creation_wrong_value():
    """Check exception when initialize Card with wrong value"""
    with pytest.raises(InvalidValue) as message:
        card = Card(20, "♥")
        assert message == "Invalid card value!"


def test_creation_wrong_color():
    """Check exception when initialize Card with wrong value"""
    with pytest.raises(InvalidColor) as message:
        card = Card(5, "HEART")
        assert message == "Invalid card color!"


def test_card_representation():
    """Check special method repr"""
    assert repr(Card(10, "♥")) == "10 -> ♥"
    assert repr(Card(2, "♣")) == "2 -> ♣"
    assert repr(Card("K", "♦")) == "K -> ♦"
    assert repr(Card("AS", "♠")) == "AS -> ♠"


def test_card_string():
    """Check special method str"""
    assert str(Card(10, "♥")) == "Card: 10♥"
    assert str(Card(2, "♣")) == "Card: 2♣"
    assert str(Card("K", "♦")) == "Card: K♦"
    assert str(Card("AS", "♠")) == "Card: AS♠"
