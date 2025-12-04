import pytest
import os
import sys

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from calculator import Calculator


def test_sequence_of_operations_results_and_history():
    calc = Calculator()

    result1 = calc.add(1, 2)         #4
    result2 = calc.multiply(result1, 5)  #15
    result3 = calc.add(result2, -5)  #10

    assert result1 == 3
    assert result2 == 15
    assert result3 == 10


def test_failing_example():
    calc = Calculator()
    assert calc.add(1, 1) == 2
