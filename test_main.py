import pytest

from main import add_numbers

def test_add_numbers():
    assert add_numbers(3, 5) == 8
    assert add_numbers(0, 0) == 0
    assert add_numbers(-34, 32) == -2
    with pytest.raises(TypeError):
        add_numbers(4.2, 3.7)
    with pytest.raises(TypeError):
        add_numbers("hello", "world")
