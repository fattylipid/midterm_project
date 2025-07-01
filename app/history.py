import pandas as pd
import os
from app.calculator_config import CalculatorConfig
from app.calculator_memento import CalculatorMemento
from app.exceptions import OperationError
from app.operations import OperationFactory
from app.calculation import Calculation

class CalculatorHistory:
    def __init__(self):
        self._history = []
        self._undo_stack = []
        self._redo_stack = []

    def add_calculation(self, calculation):
        self._undo_stack.append(self.create_memento())
        self._redo_stack.clear()
        self._history.append(calculation)

    def get_history(self):
        return self._history

    def create_memento(self):
        return CalculatorMemento(self._history)

    def undo(self):
        if not self._undo_stack:
            raise OperationError("Nothing to undo.")
        self._redo_stack.append(self.create_memento())
        memento = self._undo_stack.pop()
        self._history = memento.get_snapshot()

    def redo(self):
        if not self._redo_stack:
            raise OperationError("Nothing to redo.")
        self._undo_stack.append(self.create_memento())
        memento = self._redo_stack.pop()
        self._history = memento.get_snapshot()

    def clear(self):
        self._history.clear()
        self._undo_stack.clear()
        self._redo_stack.clear()

    def save_to_file(self):
        file_path = os.path.join(CalculatorConfig.HISTORY_DIR, "history.csv")

        data = [{
            "operation": calc.operation.__class__.__name__,
            "a": calc.a,
            "b": calc.b,
            "result": calc.result,
            "timestamp": calc.timestamp
        } for calc in self._history]

        df = pd.DataFrame(data)
        df.to_csv(file_path, index=False, encoding=CalculatorConfig.DEFAULT_ENCODING)

    def load_from_file(self):
        file_path = os.path.join(CalculatorConfig.HISTORY_DIR, "history.csv")

        if not os.path.exists(file_path):
            raise FileNotFoundError("No saved history found.")

        df = pd.read_csv(file_path)
        self._history.clear()

        for _, row in df.iterrows():
            op_class = OperationFactory.name_to_class(row["operation"])
            if not op_class:
                continue  # Skip unknown operations

            operation = op_class()
            calc = Calculation(
                operation=operation,
                a=row["a"],
                b=row["b"],
                result=row["result"],
                timestamp=row["timestamp"]
            )
            self._history.append(calc)


class AutoSaveObserver:
    def __init__(self):
        self.path = os.path.join(CalculatorConfig.HISTORY_DIR, "history.csv")

    def update(self, calculation, history):
        data = [{
            "operation": c.operation.__class__.__name__,
            "a": c.a,
            "b": c.b,
            "result": c.result,
            "timestamp": c.timestamp
        } for c in history.get_history()]

        df = pd.DataFrame(data)
        df.to_csv(self.path, index=False, encoding=CalculatorConfig.DEFAULT_ENCODING)
