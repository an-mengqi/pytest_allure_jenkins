import allure
import pytest


@allure.step("Проверяю наличие буквы 'e' в слове 'Test'")
def test_find_letter():
    """Check a letter in a word"""
    word = "Test"
    assert "e" in word


@pytest.mark.parametrize("word_part", ["wond", "wor"])
def test_find_word_parts(word_part):
    phrase = "What a wonderful world!"
    with allure.step(f"Проверяю наличие букв '{word_part}' во фразе '{phrase}'"):
        assert word_part in phrase
