class ToolkitError(Exception):
    """Базовая ошибка приложения toolkit."""


class ToolkitValidationError(ToolkitError):
    """Ошибка проверки арифметического выражения."""


class ToolkitTokenizerError(ToolkitError):
    """Ошибка разбиения выражения на токены."""


class ToolkitCalculateError(ToolkitError):
    """Ошибка вычисления арифметического выражения."""


class ToolkitConverterError(ToolkitError):
    """Ошибка преобразования единиц измерения."""