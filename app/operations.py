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

class OperationFactory:
    @staticmethod
    def get_operation(name: str):
        operations = {
            "add": AddOperation,
            "power": PowerOperation
        }
        op_class = operations.get(name.lower())
        if not op_class:
            raise OperationError(f"Operation '{name}' is not supported.")
        return op_class()