class Calculator:

    def __init__(self):
        self._history = []

    def add(self, a: float, b: float) -> float:
        result = a + b
        self._history.append(("add", a, b, result))
        return result

    def multiply(self, a: float, b: float) -> float:
        result = a * b
        self._history.append(("multiply", a, b, result))
        return result

    def history(self):
        return list(self._history)

    def clear_history(self):
        self._history.clear()
