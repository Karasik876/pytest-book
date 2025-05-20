import pytest
from cards import Card

def test_start_from_done(cards_db):
    index = cards_db.add_card(Card(summary="some thing", state="done"))
    cards_db.start(index)
    card = cards_db.get_card(index)
    assert card.state == "in prog"

def test_start_from_in_prog(cards_db):
    index = cards_db.add_card(Card(summary="some thing2", state="in prog"))
    cards_db.start(index)
    card = cards_db.get_card(index)
    assert card.state == "in prog"

def test_start_from_todo(cards_db):
    index = cards_db.add_card(Card(summary="some thing3", state="todo"))
    cards_db.start(index)
    card = cards_db.get_card(index)
    assert card.state == "in prog"

@pytest.mark.parametrize(
    "start_state",
    [
        "done",
        "in prog",
        "todo"
    ]
)
def test_start_parametrized(cards_db, start_state):
    index = cards_db.add_card(Card(summary="some thing", state=start_state))
    cards_db.start(index)
    card = cards_db.get_card(index)
    assert card.state == "in prog"

@pytest.fixture(params=('done', 'in prog', 'todo'))
def start_card(cards_db, request):
    if request.param != "todo":
        index = cards_db.add_card(Card(summary="some thing", state=request.param))
        cards_db.start(index)
        card = cards_db.get_card(index)
        return card.state
    return "todo"

def test_start_fixture_params(cards_db, start_card):
    if start_card == "todo":
        with pytest.raises(AssertionError):
            assert start_card == "in prog"
    else:
        assert start_card == "in prog"


def pytest_generate_tests(metafunc):
    print(metafunc)
    if "gggg" in metafunc.fixturenames:
        metafunc.parametrize("gggg", ["done", "in prog", "todo"])
    if "second_fixture" in metafunc.fixturenames:
        metafunc.parametrize("second_fixture", [{"hero": "pudge", "side": "dire", "mmr": "5000"}, {"hero": "invoker", "side": "radiant", "mmr": "10000"}, {"hero": "viper", "side": "dire", "mmr": "9999"}])
def test_start_generate(cards_db, gggg, second_fixture):

    print( "\n", gggg, "\n",second_fixture)
    assert second_fixture is not None
    assert isinstance(second_fixture, dict)

    c = Card(summary="some thing", state=gggg)
    index = cards_db.add_card(c)
    cards_db.start(index)
    card = cards_db.get_card(index)
    assert card.state == "in prog"
