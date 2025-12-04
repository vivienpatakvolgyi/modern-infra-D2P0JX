import pytest
import os
import sys

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from calculator import Calculator



@pytest.fixture
def calc():
    return Calculator()


def test_add_positive_numbers(calc):
    assert calc.add(2, 3) == 5


def test_multiply_by_zero(calc):
    assert calc.multiply(10, 0) == 0


def test_history_stores_operations(calc):
    calc.add(1, 2)
    calc.multiply(2, 3)
    history = calc.history()

    assert len(history) == 2
    assert history[0][0] == "add"
    assert history[1][0] == "multiply"

