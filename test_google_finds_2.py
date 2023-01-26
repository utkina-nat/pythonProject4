import pytest


@pytest.fixture()
def before_each():
    print("Called before each test")


def test_first(before_each):
    assert 1 == 1
