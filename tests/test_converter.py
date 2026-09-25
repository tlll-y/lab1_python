import pytest

from toolkit.converter import convert
from toolkit.errors import ToolkitConverterError


def test_convert_centimeters_to_meters():
    assert convert(100, "cm", "m") == 1.0


def test_convert_kilometers_to_meters():
    assert convert(2, "km", "m") == 2000.0


def test_convert_kilograms_to_grams():
    assert convert(2, "kg", "g") == 2000.0


def test_convert_grams_to_kilograms():
    assert convert(500, "g", "kg") == 0.5


def test_convert_celsius_to_fahrenheit():
    assert convert(0, "c", "f") == 32.0


def test_convert_fahrenheit_to_celsius():
    assert convert(32, "f", "c") == 0.0


def test_convert_celsius_to_kelvin():
    assert convert(0, "c", "k") == 273.15


def test_convert_kelvin_to_celsius():
    assert convert(273.15, "k", "c") == 0.0


def test_convert_units_case_insensitive():
    assert convert(100, "Cm", "M") == 1.0


def test_unknown_from_unit():
    with pytest.raises(ToolkitConverterError):
        convert(10, "abc", "m")


def test_unknown_to_unit():
    with pytest.raises(ToolkitConverterError):
        convert(10, "m", "abc")


def test_incompatible_units():
    with pytest.raises(ToolkitConverterError):
        convert(10, "cm", "kg")


def test_temperature_below_absolute_zero_celsius():
    with pytest.raises(ToolkitConverterError):
        convert(-300, "c", "k")


def test_temperature_below_absolute_zero_fahrenheit():
    with pytest.raises(ToolkitConverterError):
        convert(-500, "f", "c")


def test_temperature_below_absolute_zero_kelvin():
    with pytest.raises(ToolkitConverterError):
        convert(-1, "k", "c")
