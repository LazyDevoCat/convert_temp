# -*- encoding: utf-8 -*-
import argparse
from converter.converter import *

CELSIUM_INPUT = ['celsius', 'cels', 'cel', '-c', 'c']
FAH_INPUT = ['fahrenheit', 'fahren', 'far', '-f', 'f']
QUIT_INPUT = ['quit', 'q', 'exit']

parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", help="It just return your argument")
parser.add_argument("-f", "--fahrenheit", help="Take temperature in Fahrenheit and convert to Celsius", type=float)
parser.add_argument("-c", "--celsius", help="Take temperature in Celsius and convert to Fahrenheit", type=float)

args = parser.parse_args()


def check_number(arg):
    """
    Check if the user's input convertible to float type
    """
    try:
        float(arg)
        return float(arg)
    except ValueError:
        return False


if args.verbose:
    print(str(args) + " It's verbose argument")
elif args.fahrenheit:
    # print(f"{args.fahrenheit} Fahrenheit")
    print(fahren_to_cel(args.fahrenheit))
elif args.celsius:
    # print(f"{args.celsius} Celsius")
    print(cel_to_fahren(args.celsius))
else:
    answer = str(input("What temperature you want convert?: ")).lower()
    
    while answer not in (CELSIUM_INPUT + FAH_INPUT):
        answer = str(input("What temperature you want convert?: ")).lower()
        if answer in QUIT_INPUT:
            break
    
    if answer in CELSIUM_INPUT:  # Convert from Celsius to Fahrenheit
        celsius = input("Provide temperature in Celsius: ")
        if check_number(celsius):
            print(cel_to_fahren(float(celsius)))
        else:
            print(f"ERROR: {celsius} is not convertible to float type")
    
    if answer in FAH_INPUT:  # Convert from Fahrenheit to Celsius
        fahrenheit = input("Provide temperature in Fahrenheit: ")
        if check_number(fahrenheit):
            print(fahren_to_cel(float(fahrenheit)))
        else:
            print(f"ERROR: {fahrenheit} is not convertible to float type")
