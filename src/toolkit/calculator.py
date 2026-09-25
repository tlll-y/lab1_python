from src.toolkit.errors import ToolkitCalculateError
from toolkit.validator import validate_tokens


def calculate(tokens: list[str]) -> float:
    """Вычисляет арифметическое выражение, представленное токенами."""
    validate_tokens(tokens)

    values = []
    operators = []

    index = 0
    expecting_number = True

    while index < len(tokens):
        token = tokens[index]

        if token in "+-" and expecting_number:
            number = float(tokens[index + 1])

            if token == "-":
                number = -number

            values.append(number)
            index += 2

            expecting_number = False

        elif token in "*/" or token in "+-":
            operators.append(token)
            index += 1
            expecting_number = True

        else:
            values.append(float(token))
            index += 1
            expecting_number = False

    index = 0

    while index < len(operators):
        operator = operators[index]

        if operator in "*/":
            left = values[index + 0]
            right = values[index + 1]
            if operator == "*":
                result = left * right
            else:
                if right == 0:
                    raise ToolkitCalculateError("Division by zero")
                result = left / right

            values.pop(index)
            values.pop(index)
            values.insert(index, result)
            operators.pop(index)
        else:
            index += 1

    result = values[0]

    index = 0

    while index < len(operators):
        operator = operators[index]
        right = values[index + 1]

        if operator == "+":
            result += right
        else:
            result -= right

        index += 1

    return result
