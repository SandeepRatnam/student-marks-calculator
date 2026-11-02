
from calculator import add, multiply


def test_add():
    assert add(10, 20) == 30


def test_multiply():
    assert multiply(10, 20) == 200


def test_add_with_negative_number():
    assert add(-5, 10) == 5
