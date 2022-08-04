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
import argparse # For parsing arguments when run script



def cel_to_fahren(tempreture_in_celsium):
    fahren = (tempreture_in_celsium * (9 / 5)) + 32
    return fahren

def fahren_to_cel(temprutere_in_fahren):
    cels = (5 / 9) * (temprutere_in_fahren - 32)
    return cels


answer = str(input("What teamprute you want convert?: ")).lower()

if answer in ['celsius', 'cels', 'cel']:  # Convert from Celsius to Fahrenheit
    celsium = float(input("Provide tempruture in Celsius: "))
    print(cel_to_fahren(celsium))

elif answer in ['fahrenheit', 'fahren', 'far']: # Convert from Fahrenheit to Celsius
    fahrenheit = float(input("Provide tempruture in Fahrenheit: "))
    print(fahren_to_cel(fahrenheit))

else:
    pass


