"""
You need to create a github repo (public), plan project structure, use MIT license. 
Also you need to decide how to run two different conversions with a single script, e.g. how to decide which conversion you have to perform.

From Celsius  to Fahrenheit
Temp: 20 C
20 * (9/5) + 32 = 68 F


From Fahrenheit to Celsius
Temp: 68 F
(5/9) * (68 - 32) = 20 C

"""
import argparse  # For parsing arguments when run script


def cel_to_fahren(tempreture_in_celsium):  # Take temperature in Celsius and convert to Fahrenheit
    fahren = (tempreture_in_celsium * (9 / 5)) + 32
    return fahren


def fahren_to_cel(temprutere_in_fahren):  # Take temperature in Fahrenheit and convert to Celsius
    cels = (5 / 9) * (temprutere_in_fahren - 32)
    return cels


parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", help="It just return your argument")
parser.add_argument("-f", help="Take temperature in Fahrenheit and convert to Celsius")
parser.add_argument("-c", help="Take temperature in Celsius and convert to Fahrenheit")

args = parser.parse_args()

if args.verbose:
    print(str(args) + " It's verbose argument")
elif args.f:
    # print(f"{args.f} Fahrenheit")
    print(fahren_to_cel(int(args.f)))
elif args.c:
    # print(f"{args.c} Celsius")
    print(cel_to_fahren(int(args.c)))
else:
    answer = str(input("What teamprute you want convert?: ")).lower()
    
    if answer in ['celsius', 'cels', 'cel', '-c']:  # Convert from Celsius to Fahrenheit
        celsium = float(input("Provide tempruture in Celsius: "))
        print(cel_to_fahren(celsium))
    
    elif answer in ['fahrenheit', 'fahren', 'far', '-f']:  # Convert from Fahrenheit to Celsius
        fahrenheit = float(input("Provide tempruture in Fahrenheit: "))
        print(fahren_to_cel(fahrenheit))
    
    else:
        pass
