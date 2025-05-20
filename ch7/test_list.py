"""
Test Cases
* `list` from an empty database
* `list` from a non-empty database
"""
import pytest
from cards import Card


def test_list_no_cards(cards_db):
    """Empty db, empty list"""
    assert cards_db.list_cards() == []


def test_list_several_cards(cards_db):
    """
    Given a variety of cards, make sure they get returned.
    """
    orig = [
        Card("foo"),
        Card("bar", owner="me"),
        Card("baz", owner="you", state="in prog"),
    ]

    for c in orig:
        cards_db.add_card(c)

    the_list = cards_db.list_cards()

    assert len(the_list) == len(orig)
    for c in orig:
        assert c in the_list

@pytest.mark.parametrize(
    "card_owner, card_state",
    (
        ("you", None),
        (None, "todo"),
        ("you", "in prog")
    )
)
def test_list_filter(cards_db, card_owner, card_state):
    orig = [
        Card("foo"),
        Card("bar", owner="me"),
        Card("foobar", state="in prog"),
        Card("foobaz", owner=card_owner, state="todo"),
        Card("foofoo", owner="me", state=card_state),
        Card("baz", owner=card_owner, state=card_state),
    ]

    for c in orig:
        cards_db.add_card(c)

    the_list = cards_db.list_cards(owner=card_owner, state=card_state)

    for c in the_list:
        if card_state is not None:
            assert c.state == card_state
        if card_owner is not None:
            assert c.owner == card_owner
