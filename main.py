from app.calculator import Calculator
from app.operations import OperationFactory
from app.input_validators import validate_number, validate_within_range
from app.calculator_config import CalculatorConfig
from app.logger import LoggerObserver
from app.history import AutoSaveObserver

def run_repl():
    CalculatorConfig.ensure_directories()
    calc = Calculator()

    # Register observers
    calc.register_observer(LoggerObserver())
    if CalculatorConfig.AUTO_SAVE:
        calc.register_observer(AutoSaveObserver())

    # ✅ Define this BEFORE it's used
    valid_commands = [
        "add", "power", "root", "modulus",
        "int_divide", "percent", "abs_diff"
    ]

    print("Welcome to Enhanced Calculator. Type 'help' for commands.")

    while True:
        try:
            command = input("> ").strip().lower()

            if command == "exit":
                print("Goodbye!")
                break

            elif command == "help":
                print("""Available commands:
add, power, root, modulus, int_divide, percent, abs_diff
history, undo, redo, clear, save, load, help, exit
""")

            elif command in valid_commands:
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

            elif command == "undo":
                calc.history.undo()
                print("Last calculation undone.")

            elif command == "redo":
                calc.history.redo()
                print("Redo successful.")

            elif command == "clear":
                calc.history.clear()
                print("History cleared.")

            elif command == "save":
                calc.history.save_to_file()
                print("History saved.")

            elif command == "load":
                calc.history.load_from_file()
                print("History loaded.")

            else:
                print("Unknown command. Type 'help' to see available options.")

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    run_repl()
