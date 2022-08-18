# -*- encoding: utf-8 -*-
"""
This file contains converter logic

1. Convert temperature:
    Converting from Fahrenheit to Celsius and vice versa are available
"""

# Convert temperature


def celsius_to_fahrenheit(temperature_in_celsius: float) -> float:
    """
    Take temperature in Celsius and convert to Fahrenheit
    Temp: 20 C
    20 * (9/5) + 32 = 68 F
    """
    fahrenheit = round(((temperature_in_celsius * (9 / 5)) + 32), 1)
    return fahrenheit


def fahrenheit_to_celsius(temperature_in_fahrenheit: float) -> float:
    """
    Take temperature in Fahrenheit and convert to Celsius
    Temp: 68 F
    (5/9) * (68 - 32) = 20 C
    """
    celsius = round((5 / 9) * (temperature_in_fahrenheit - 32), 1)
    return celsius
