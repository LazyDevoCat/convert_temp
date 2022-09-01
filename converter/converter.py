# -*- encoding: utf-8 -*-
"""
This file contains converter logic

1. Convert temperature:
    Converting from Fahrenheit to Celsius and vice versa are available

Raise taken here
_https://www.pythontutorial.net/python-oop/python-custom-exception/
"""
from abc import ABC, abstractmethod

from converter.exception import TemperatureError, ConverterError

ABSOLUTE_ZERO_FAR = -459.67
ABSOLUTE_ZERO_CEL = -273.15


def celsius_to_fahrenheit(temperature_in_celsius: float) -> float:
    """
    Take temperature in Celsius and convert to Fahrenheit
    Temp: 20 C
    20 * (9/5) + 32 = 68 F
    """
    if temperature_in_celsius < ABSOLUTE_ZERO_CEL:
        raise TemperatureError(temperature_in_celsius, ABSOLUTE_ZERO_CEL)
    else:
        return round(((temperature_in_celsius * (9 / 5)) + 32), 1)


def fahrenheit_to_celsius(temperature_in_fahrenheit: float) -> float:
    """
    Take temperature in Fahrenheit and convert to Celsius
    Temp: 68 F
    (5/9) * (68 - 32) = 20 C
    """
    if temperature_in_fahrenheit < ABSOLUTE_ZERO_FAR:
        raise TemperatureError(temperature_in_fahrenheit, ABSOLUTE_ZERO_FAR)
    else:
        return round(((5 / 9) * (temperature_in_fahrenheit - 32)), 1)


def get_convertor_function(fahrenheit: bool, celsius: bool) -> callable:
    if fahrenheit:
        return fahrenheit_to_celsius
    if celsius:
        return celsius_to_fahrenheit
    raise ConverterError("Can not find suitable convertor function")


class ConverterContext(ABC):

    @abstractmethod
    def get_converter_function(self):
        pass

    @abstractmethod
    def get_temperature(self):
        pass
