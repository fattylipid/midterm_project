from datetime import datetime

class Calculation:
    def __init__(self, operation, a, b, result, timestamp=None):
        self.operation = operation
        self.a = a
        self.b = b
        self.result = result
        self.timestamp = timestamp or datetime.now()

    def __str__(self):
        return f"[{self.timestamp}] {self.operation.__class__.__name__}({self.a}, {self.b}) = {self.result}"
