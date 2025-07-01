from app.calculation import Calculation
from app.operations import AddOperation

def test_calculation_str():
    op = AddOperation()
    calc = Calculation(op, 2, 3, 5)
    result_str = str(calc)
    
    assert "AddOperation" in result_str
    assert "(2, 3)" in result_str
    assert "= 5" in result_str
