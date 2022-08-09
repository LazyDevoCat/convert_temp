# This file contains converter logic

# Convert temperature

def cel_to_fahren(tempreture_in_celsium):
    """
    Take temperature in Celsius and convert to Fahrenheit
    Temp: 20 C
    20 * (9/5) + 32 = 68 F
    """
    fahren = (tempreture_in_celsium * (9 / 5)) + 32
    return fahren


def fahren_to_cel(temprutere_in_fahren):
    """
    Take temperature in Fahrenheit and convert to Celsius
    Temp: 68 F
    (5/9) * (68 - 32) = 20 C
    """
    cels = (5 / 9) * (temprutere_in_fahren - 32)
    return cels
