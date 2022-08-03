"""
You need to create a github repo (public), plan project structure, use MIT license. 
Also you need to decide how to run two different conversions with a single script, e.g. how to decide which conversion you have to perform

From Celsius  to Fahrenheit
Temp: 20 C
20 * (9/5) + 32 = 68 F


From Fahrenheit to Celsius
Temp: 68 F
(5/9) * (68 - 32) = 20 C

"""


def cel_to_fahren(tempreture_in_celsium):
    fahren = (tempreture_in_celsium * (9 / 5)) + 32
    return fahren

celsium = float(input("Provide tempruture: "))

print(cel_to_fahren(celsium))