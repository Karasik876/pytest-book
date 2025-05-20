import pytest


def hello():
    with open("hello.txt", "w") as f:
        f.write("Hello World!\n")



def test_hello():
    hello()
    with open("hello.txt") as file:
        assert file.read().rstrip() == "Hello World!"



@pytest.fixture()
def hello_fix(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    hello()
    print(tmp_path)

def test_hello_fix(hello_fix):
    with open("hello.txt") as file:
        assert file.read().rstrip() == "Hello World!"


