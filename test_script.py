import pytest
from script import add,subtract,multiply,divide

def test_add():
    assert add(1,2) == 3
    assert add(-1,1) == 0

def test_subtract():
    assert subtract(1,2) == -1
    assert subtract(5,3) == 2

def test_multiply():
    assert multiply(1,2) == 2
    assert multiply(-1,1) == -1

def test_divide():
    assert divide(1,1) == 1
    with pytest.raises(ValueError):
        divide(1,0)