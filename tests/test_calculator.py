from app.calculator import Calculator
from app.operations import AddOperation

def test_perform_operation_and_history():
    calc = Calculator()
    result = calc.perform_operation(AddOperation(), 4, 5)
    assert result == 9
    assert len(calc.history.get_history()) == 1
