from app.logger import LoggerObserver
from app.history import CalculatorHistory
from app.operations import AddOperation
from app.calculation import Calculation

def test_logger_does_not_crash(tmp_path):
    import logging
    from app.calculator_config import CalculatorConfig
    CalculatorConfig.LOG_DIR = str(tmp_path)
    LoggerObserver().update(
        Calculation(AddOperation(), 1, 1, 2),
        CalculatorHistory()
    )
    assert True