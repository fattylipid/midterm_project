import os
from app.calculator_config import CalculatorConfig

def test_config_defaults_exist():
    assert isinstance(CalculatorConfig.MAX_HISTORY_SIZE, int)
    assert CalculatorConfig.AUTO_SAVE in [True, False]
    assert CalculatorConfig.PRECISION >= 0
    assert CalculatorConfig.MAX_INPUT_VALUE > 0

def test_ensure_directories(tmp_path):
    # Temporarily patch log/history dirs
    CalculatorConfig.LOG_DIR = os.path.join(tmp_path, "logs")
    CalculatorConfig.HISTORY_DIR = os.path.join(tmp_path, "history")
    CalculatorConfig.ensure_directories()

    assert os.path.exists(CalculatorConfig.LOG_DIR)
    assert os.path.exists(CalculatorConfig.HISTORY_DIR)
