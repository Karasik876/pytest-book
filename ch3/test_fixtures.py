"""Demonstrate simple fixtures."""

import pytest


@pytest.fixture()
def r_dict():
    print('pudge1')
    yield {'1': 'dismember', '2': 'black hole', '3': 'assasinate'}
    print('pudge2')
@pytest.fixture(scope="module")
def r_tuple():
    print('pudge start')
    yield ('pudge;dismember', 'enigma;black hole', 'sniper;assasinate' )
    print('pudge finish')

def test_dict(r_dict, r_tuple):
    assert type(r_dict) is dict

def test_tuple(r_tuple, r_dict):
    assert type(r_tuple) is tuple
    assert r_dict != r_tuple
    for i in range(3):
        assert r_dict[str(i+1)] == r_tuple[i].split(";")[1]
