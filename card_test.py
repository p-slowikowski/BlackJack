from card import Card


def test_creation():
    card = Card(10, "♥")
    assert card.color == "♥"
    assert card.value == 10
