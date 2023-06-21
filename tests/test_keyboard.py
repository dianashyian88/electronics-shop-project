"""Здесь надо написать тесты с использованием pytest для модуля keyboard."""
from src.keyboard import KeyBoard


def test_str():
    kb = KeyBoard('Dark Project KD87A', 9600, 5)
    assert str(kb) == "Dark Project KD87A"
    assert str(kb.language) == "EN"


def test_change_lang():
    kb = KeyBoard('Dark Project KD87A', 9600, 5)
    kb.change_lang()
    assert str(kb.language) == "RU"
    kb.change_lang().change_lang()
    assert str(kb.language) == "RU"
    kb.language = 'CH'
