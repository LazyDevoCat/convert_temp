# -*- encoding: utf-8 -*-
"""
This file contains converter logic

1. Convert temperature (converting from Fahrenheit to Celsius and vice versa are available)
"""

# Convert temperature


def cel_to_fahren(temperature_in_celsium: float):
    """
    Take temperature in Celsius and convert to Fahrenheit
    Temp: 20 C
    20 * (9/5) + 32 = 68 F
    """
    fahren = round(((temperature_in_celsium * (9 / 5)) + 32), 1)
    return fahren


def fahren_to_cel(temperature_in_fahren: float):
    """
    Take temperature in Fahrenheit and convert to Celsius
    Temp: 68 F
    (5/9) * (68 - 32) = 20 C
    """
    cels = round((5 / 9) * (temperature_in_fahren - 32), 1)
    return cels
