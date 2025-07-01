class CalculatorError(Exception):
    """Base class for all calculator-related errors."""
    pass

class OperationError(CalculatorError):
    """Raised when an operation fails (e.g. divide by zero)."""
    pass

class ValidationError(CalculatorError):
    """Raised when input is invalid."""
    pass
