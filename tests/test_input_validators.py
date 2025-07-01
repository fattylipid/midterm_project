import pytest
from app.input_validators import validate_number, validate_within_range
from app.exceptions import ValidationError

def test_validate_number_valid():
    assert validate_number("3.14") == 3.14

def test_validate_number_invalid():
    with pytest.raises(ValidationError):
        validate_number("abc")

def test_validate_within_range_valid():
    assert validate_within_range(999, 1000) == 999

def test_validate_within_range_exceeds():
    with pytest.raises(ValidationError):
        validate_within_range(1001, 1000)
