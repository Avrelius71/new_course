import pytest

def test_input():
    x = input('Set a phrase: ')
    assert len(x) < 15, 'Фраза должна быть короче 15 символов'