from greeting import greeting
import pytest
tests = [('Никита', 'Привет, Никита'), ('Ольга', 'Привет, Ольга'), ('Андрей', 'Привет, Андрей')]

@pytest.mark.parametrize('name,expected', tests)
def test_greeting(name: str, expected: str):
    assert greeting(name) == expected
