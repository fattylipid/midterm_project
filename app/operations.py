from abc import ABC, abstractmethod
from app.exceptions import OperationError

class Operation(ABC):
    @abstractmethod
    def execute(self, a: float, b: float) -> float:
        pass

class AddOperation(Operation):
    def execute(self, a: float, b: float) -> float:
        return a + b

class PowerOperation(Operation):
    def execute(self, a: float, b: float) -> float:
        return a ** b

class RootOperation(Operation):
    def execute(self, a: float, b: float) -> float:
        if b == 0:
            raise OperationError("Cannot take root with b=0.")
        return a ** (1 / b)

class ModulusOperation(Operation):
    def execute(self, a: float, b: float) -> float:
        if b == 0:
            raise OperationError("Cannot perform modulus with b=0.")
        return a % b

class IntegerDivisionOperation(Operation):
    def execute(self, a: float, b: float) -> float:
        if b == 0:
            raise OperationError("Cannot divide by zero.")
        return a // b

class PercentageOperation(Operation):
    def execute(self, a: float, b: float) -> float:
        if b == 0:
            raise OperationError("Cannot calculate percentage with b=0.")
        return (a / b) * 100

class AbsoluteDifferenceOperation(Operation):
    def execute(self, a: float, b: float) -> float:
        return abs(a - b)

class OperationFactory:
    operations = {
        "add": AddOperation,
        "power": PowerOperation,
        "root": RootOperation,
        "modulus": ModulusOperation,
        "int_divide": IntegerDivisionOperation,
        "percent": PercentageOperation,
        "abs_diff": AbsoluteDifferenceOperation
        }
    @staticmethod
    def get_operation(name: str):
        op_class = OperationFactory.operations.get(name.lower())
        if not op_class:
            raise OperationError(f"Operation '{name}' is not supported.")
        return op_class()

    @staticmethod
    def name_to_class(name: str):
        for op in OperationFactory.operations.values():
            if op.__name__ == name:
                return op
        return None