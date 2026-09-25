from toolkit.calculator import calculate
from toolkit.errors import (
    ToolkitCalculateError,
    ToolkitTokenizerError,
    ToolkitValidationError,
)
from toolkit.tokenizer import tokenize
from toolkit.validator import validate_tokens


def test_tokenize_simple_expression():
    assert tokenize("2 + 3") == ["2", "+", "3"]


def test_tokenize_expression_without_spaces():
    assert tokenize("12*3") == ["12", "*", "3"]


def test_tokenize_float_numbers():
    assert tokenize("12.5 / 2") == ["12.5", "/", "2"]


def test_tokenize_ignores_spaces():
    assert tokenize("  2   +   3  ") == ["2", "+", "3"]


def test_tokenize_invalid_character():
    try:
        tokenize("2 & 3")
    except ToolkitTokenizerError:
        pass
    else:
        raise AssertionError("Expected ToolkitTokenizerError")


def test_validate_valid_expression():
    validate_tokens(["2", "+", "3"])


def test_validate_unary_minus():
    validate_tokens(["2", "*", "-", "3"])


def test_validate_unary_plus():
    validate_tokens(["+", "5"])


def test_validate_empty_expression():
    try:
        validate_tokens([])
    except ToolkitValidationError:
        pass
    else:
        raise AssertionError("Expected ToolkitValidationError")


def test_validate_two_operators_in_row():
    try:
        validate_tokens(["2", "*", "/", "3"])
    except ToolkitValidationError:
        pass
    else:
        raise AssertionError("Expected ToolkitValidationError")


def test_validate_expression_ending_with_operator():
    try:
        validate_tokens(["2", "+"])
    except ToolkitValidationError:
        pass
    else:
        raise AssertionError("Expected ToolkitValidationError")


def test_calculate_addition():
    assert calculate(["2", "+", "3"]) == 5.0


def test_calculate_subtraction():
    assert calculate(["10", "-", "3"]) == 7.0


def test_calculate_multiplication():
    assert calculate(["4", "*", "5"]) == 20.0


def test_calculate_division():
    assert calculate(["10", "/", "2"]) == 5.0


def test_calculate_operator_precedence():
    assert calculate(["2", "+", "3", "*", "4"]) == 14.0


def test_calculate_division_by_zero():
    try:
        calculate(["10", "/", "0"])
    except ToolkitCalculateError:
        pass
    else:
        raise AssertionError("Expected ToolkitCalculateError")


def test_calculate_unary_minus():
    assert calculate(["-", "5"]) == -5.0


def test_calculate_unary_plus():
    assert calculate(["+", "5"]) == 5.0


def test_calculate_unary_minus_after_multiplication():
    assert calculate(["2", "*", "-", "3"]) == -6.0


def test_calculate_two_unary_minus():
    assert calculate(["-", "2", "*", "-", "3"]) == 6.0


def test_tokenize_number_starting_with_dot():
    assert tokenize(".5 + 1") == [".5", "+", "1"]


def test_calculate_number_starting_with_dot():
    assert calculate([".5", "+", "1"]) == 1.5
