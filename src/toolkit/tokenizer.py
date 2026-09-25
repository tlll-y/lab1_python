from toolkit.errors import ToolkitTokenizerError


def tokenize(expression: str) -> list[str]:
    """Разбивает арифметическое выражение на отдельные токены."""
    tokens = []
    current_number = ""

    for char in expression:
        if char.isspace():
            if current_number:
                tokens.append(current_number)
                current_number = ""
            continue

        if char.isdigit() or char == ".":
            current_number += char
            continue

        if current_number:
            tokens.append(current_number)
            current_number = ""

        if char in "+-*/":
            tokens.append(char)
            continue

        raise ToolkitTokenizerError(
            f"Invalid character: {char}")

    if current_number:
        tokens.append(current_number)

    return tokens
