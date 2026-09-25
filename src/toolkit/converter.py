from toolkit.constants import LENGTH_UNITS, MASS_UNITS, TEMPERATURE_UNITS
from toolkit.errors import ToolkitConverterError


def get_unit_group(unit: str) -> str:
    """Определяет группу единицы измерения."""
    if unit in LENGTH_UNITS:
        return "length"

    if unit in MASS_UNITS:
        return "mass"

    if unit in TEMPERATURE_UNITS:
        return "temperature"

    raise ToolkitConverterError(f"Unknown unit: {unit}")


def convert(value: float, from_unit: str, to_unit: str) -> float:
    """Преобразует значение из одной единицы измерения в другую."""
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    from_group = get_unit_group(from_unit)
    to_group = get_unit_group(to_unit)

    if from_group != to_group:
        raise ToolkitConverterError("Incompatible units")

    if from_group in ("length", "mass"):
        if from_group == "length":
            units = LENGTH_UNITS
        else:
            units = MASS_UNITS

        base_value = value * units[from_unit]
        result = base_value / units[to_unit]

        return float(result)

    if from_group == "temperature":
        absolute_zero = {
            "c": -273.15,
            "f": -459.67,
            "k": 0.0,
        }

        if value < absolute_zero[from_unit]:
            raise ToolkitConverterError("Temperature below absolute zero")

        if from_unit == "c":
            celsius = value
        elif from_unit == "f":
            celsius = (value - 32) * 5 / 9
        else:
            celsius = value - 273.15

        if to_unit == "c":
            result = celsius
        elif to_unit == "f":
            result = celsius * 9 / 5 + 32
        else:
            result = celsius + 273.15

        return float(result)
