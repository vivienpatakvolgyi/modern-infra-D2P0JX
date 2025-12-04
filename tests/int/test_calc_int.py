import pytest

from calculator import Calculator


def test_sequence_of_operations_results_and_history():
    calc = Calculator()

    result1 = calc.add(1, 3)         # 4
    result2 = calc.multiply(result1, 5)  # 15
    result3 = calc.add(result2, -5)  # 10

    assert result1 == 3
    assert result2 == 15
    assert result3 == 10

    history = calc.history()
    assert len(history) == 3
    assert history[0] == ("add", 1, 2, 3)
    assert history[1] == ("multiply", 3, 5, 15)
    assert history[2] == ("add", 15, -5, 10)


def test_failing_example():
    calc = Calculator()
    assert calc.add(1, 1) == 3
