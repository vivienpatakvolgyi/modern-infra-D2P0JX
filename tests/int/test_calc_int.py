import pytest

from src.calculator import Calculator


def test_sequence_of_operations_results_and_history():
    calc = Calculator()

    # „integráció”: több metódus együtt, állapot követése
    result1 = calc.add(1, 2)         # 3
    result2 = calc.multiply(result1, 5)  # 15
    result3 = calc.add(result2, -5)  # 10

    assert result1 == 3
    assert result2 == 15
    assert result3 == 10

    history = calc.history()
    assert len(history) == 3
    # ellenőrizzük a teljes integrált lefutást
    assert history[0] == ("add", 1, 2, 3)
    assert history[1] == ("multiply", 3, 5, 15)
    assert history[2] == ("add", 15, -5, 10)


# Egy direkt FAILING teszt, hogy legyen rossz run is egy PR-ben
def test_failing_example():
    # szándékosan rossz elvárás
    calc = Calculator()
    assert calc.add(1, 1) == 3
