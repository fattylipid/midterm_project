import os
import pandas as pd
from app.history import CalculatorHistory
from app.calculation import Calculation
from app.operations import AddOperation
from app.calculator_config import CalculatorConfig

def test_add_and_undo_redo():
    h = CalculatorHistory()
    calc = Calculation(AddOperation(), 1, 2, 3)
    h.add_calculation(calc)
    assert len(h.get_history()) == 1

    h.undo()
    assert len(h.get_history()) == 0

    h.redo()
    assert len(h.get_history()) == 1

def test_clear_history():
    h = CalculatorHistory()
    calc = Calculation(AddOperation(), 1, 2, 3)
    h.add_calculation(calc)
    h.clear()
    assert len(h.get_history()) == 0

def test_save_and_load(tmp_path):
    CalculatorConfig.HISTORY_DIR = tmp_path
    path = tmp_path / "history.csv"

    h = CalculatorHistory()
    h.add_calculation(Calculation(AddOperation(), 2, 2, 4))
    h.save_to_file()

    assert os.path.exists(path)

    new_history = CalculatorHistory()
    new_history.load_from_file()
    assert len(new_history.get_history()) == 1
