import allure
import pytest


@allure.step("Складываю два числа: 1 и 2")
def test_sum():
    """Check the sum of two numbers: 1 and 2"""
    summand_1 = 1
    summand_2 = 2
    assert summand_1 + summand_2 == 3


@pytest.mark.parametrize("factor_2, result", [(2, 4), (4, 8), (6, 12)])
def test_multiplication(factor_2, result):
    """Check multiplication"""
    factor_1 = 2
    with allure.step(f"Проверяю умножение {str(factor_1)} на {str(factor_2)}"):
        assert factor_1 * factor_2 == result
