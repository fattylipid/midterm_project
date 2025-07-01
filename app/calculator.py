from app.history import CalculatorHistory
from app.calculation import Calculation

class Calculator:
    def __init__(self):
        self.history = CalculatorHistory()
        self.observers = []

    def register_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self, calculation):
        for observer in self.observers:
            observer.update(calculation, self.history)

    def perform_operation(self, operation, a, b):
        result = operation.execute(a, b)
        calc = Calculation(operation, a, b, result)
        self.history.add_calculation(calc)
        self.notify_observers(calc)
        return result
