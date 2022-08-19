# -*- encoding: utf-8 -*-
"""
This file contains converter logic

1. Convert temperature:
    Converting from Fahrenheit to Celsius and vice versa are available

Raise taken here
https://www.pythontutorial.net/python-oop/python-custom-exception/
"""
from typing import Any

# ABSOLUTE_ZERO_FAR = -459.67
# ABSOLUTE_ZERO_CEL = -273.15
# Convert temperature


class TemperatureError(Exception):
    minimum_celsius = -273.15
    minimum_fahrenheit = -459.67

    def __init__(self, temperature):
        self.temperature = temperature

    def __str__(self):
        return f"Temperature {self.temperature} is not valid. " \
               f"Lower than absolute zero"


def celsius_to_fahrenheit(temperature_in_celsius: float) -> Any:
    """
    Take temperature in Celsius and convert to Fahrenheit
    Temp: 20 C
    20 * (9/5) + 32 = 68 F
    """
    try:
        if temperature_in_celsius < TemperatureError.minimum_celsius:
            raise TemperatureError(temperature_in_celsius)
    except TemperatureError as error:
        return f"{error}: -273.15"
    else:
        return round(((temperature_in_celsius * (9 / 5)) + 32), 1)


def fahrenheit_to_celsius(temperature_in_fahrenheit: float) -> Any:
    """
    Take temperature in Fahrenheit and convert to Celsius
    Temp: 68 F
    (5/9) * (68 - 32) = 20 C
    """
    try:
        if temperature_in_fahrenheit < TemperatureError.minimum_fahrenheit:
            raise TemperatureError(temperature_in_fahrenheit)
    except TemperatureError as error:
        return f"{error}: -459.67"
    else:
        return round(((5 / 9) * (temperature_in_fahrenheit - 32)), 1)

#    if temperature_in_fahrenheit < ABSOLUTE_ZERO_FAR:
#        quit(f"Error temperature couldn't be lower than {ABSOLUTE_ZERO_FAR}")
#    else:
#        celsius = round(((5 / 9) * (temperature_in_fahrenheit - 32)), 1)
#        return celsius
