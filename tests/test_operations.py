import pytest
from app.operations import (
    AddOperation, PowerOperation, RootOperation,
    ModulusOperation, IntegerDivisionOperation,
    PercentageOperation, AbsoluteDifferenceOperation
)
from app.exceptions import OperationError

def test_add():
    op = AddOperation()
    assert op.execute(3, 5) == 8

def test_power():
    op = PowerOperation()
    assert op.execute(2, 3) == 8

def test_root():
    op = RootOperation()
    assert round(op.execute(27, 3), 5) == 3.0
    with pytest.raises(OperationError):
        op.execute(9, 0)

def test_modulus():
    op = ModulusOperation()
    assert op.execute(10, 3) == 1
    with pytest.raises(OperationError):
        op.execute(5, 0)

def test_int_division():
    op = IntegerDivisionOperation()
    assert op.execute(10, 3) == 3
    with pytest.raises(OperationError):
        op.execute(10, 0)

def test_percentage():
    op = PercentageOperation()
    assert op.execute(50, 200) == 25.0
    with pytest.raises(OperationError):
        op.execute(10, 0)

def test_abs_diff():
    op = AbsoluteDifferenceOperation()
    assert op.execute(10, 4) == 6
    assert op.execute(4, 10) == 6
