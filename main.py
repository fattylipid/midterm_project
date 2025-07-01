from app.calculator import Calculator
from app.operations import OperationFactory
from app.input_validators import validate_number, validate_within_range
from app.calculator_config import CalculatorConfig

def run_repl():
    calc = Calculator()
    CalculatorConfig.ensure_directories()

    print("Welcome to Enhanced Calculator. Type 'help' for commands.")
    
    while True:
        try:
            command = input("> ").strip().lower()

            if command == "exit":
                print("Goodbye!")
                break
            elif command == "help":
                print("Commands: add, power, history, exit")
            elif command in ["add", "power"]:
                a = validate_number(input("Enter first number: "))
                b = validate_number(input("Enter second number: "))
                a = validate_within_range(a, CalculatorConfig.MAX_INPUT_VALUE)
                b = validate_within_range(b, CalculatorConfig.MAX_INPUT_VALUE)

                operation = OperationFactory.get_operation(command)
                result = calc.perform_operation(operation, a, b)
                print(f"Result: {round(result, CalculatorConfig.PRECISION)}")
            elif command == "history":
                for c in calc.history.get_history():
                    print(c)
            else:
                print("Unknown command.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    run_repl()
