import logging
import os
from app.calculator_config import CalculatorConfig

class LoggerObserver:
    def __init__(self):
        log_path = os.path.join(CalculatorConfig.LOG_DIR, "calculator.log")
        logging.basicConfig(
            filename=log_path,
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s",
        )

    def update(self, calculation, history):
        logging.info(
            f"{calculation.operation.__class__.__name__}({calculation.a}, {calculation.b}) = {calculation.result}"
        )
