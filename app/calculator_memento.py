class CalculatorMemento:
    def __init__(self, history_snapshot):
        self._snapshot = list(history_snapshot)

    def get_snapshot(self):
        return self._snapshot
