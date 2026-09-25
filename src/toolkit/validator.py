from toolkit.errors import ToolkitValidationError


def validate_tokens(tokens: list[str]) -> None:
    """Проверяет корректность последовательности токенов."""
    if not tokens:
        raise ToolkitValidationError("Empty expression")

    expecting_number = True
    unary_sign_allowed = True
    previous_was_binary_operator = False

    for token in tokens:
        if expecting_number:
            if token in "+-":
                if not unary_sign_allowed:
                    raise ToolkitValidationError("Two unary signs in a row")

                unary_sign_allowed = False
                previous_was_binary_operator = False
                continue

            try:
                float(token)
            except ValueError:
                if previous_was_binary_operator:
                    raise ToolkitValidationError("More than one binary operator in a row")
                raise ToolkitValidationError(f"Expected number, got: {token}")

            expecting_number = False
            unary_sign_allowed = True
            previous_was_binary_operator = False

        else:
            if token in "*/+-":
                if token in "*/":
                    if previous_was_binary_operator:
                        raise ToolkitValidationError("More than one binary operator in a row")

                    previous_was_binary_operator = True

                else:
                    previous_was_binary_operator = True

                expecting_number = True
                unary_sign_allowed = True
            else:
                raise ToolkitValidationError(f"Expected operator, got: {token}")

    if expecting_number:
        raise ToolkitValidationError("Expression cannot end with an operator")
