from app.exceptions import ValidationError

def validate_number(value: str) -> float:
    try:
        return float(value)
    except ValueError:
        raise ValidationError(f"'{value}' is not a valid number.")

def validate_within_range(value: float, max_value: float) -> float:
    if abs(value) > max_value:
        raise ValidationError(f"Value {value} exceeds the allowed range.")
    return value
