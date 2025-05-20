import cards
import pytest


def test_no_path_fail():
    with pytest.raises(TypeError):
        cards.CardsDB()

