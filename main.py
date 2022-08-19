# -*- encoding: utf-8 -*-
import argparse
import sys
from converter.converter import fahrenheit_to_celsius, celsius_to_fahrenheit
from converter.utils import is_float

CELSIUM_INPUT = ['celsius', 'cels', 'cel', '-c', 'c']
FAH_INPUT = ['fahrenheit', 'fahren', 'far', '-f', 'f']
QUIT_INPUT = ['quit', 'q', 'exit']

parser = argparse.ArgumentParser(
    # usage="python main.py -f or -c [value]",
    description="Take temperature in Fahrenheit(Celsius) "
                "and convert to Celsius(Fahrenheit)"
)
parser.add_argument(
    "-v", "--verbose", help="It just return your argument"
)

parser.add_argument(
    "-f", "--fahrenheit", type=float,
    help="Take temperature in Fahrenheit and convert to Celsius"
)
parser.add_argument(
    "-c", "--celsius", type=float,
    help="Take temperature in Celsius and convert to Fahrenheit"
)

# parser.add_argument(
#     "temperature", type=float,
#     help="temperature", action="store", nargs=1
# )
#
# scale_group = parser.add_mutually_exclusive_group(required=True)
#
# scale_group.add_argument(
#     "-f", "--fahrenheit", action="store_true",
#     help="use flag -f(--fahrenheit) and provide one value for converting"
# )
#
# scale_group.add_argument(
#     "-c", "--celsius", action="store_true",
#     help="use flag -c(--celsius) and provide one value for converting"
# )

args = parser.parse_args()
# print(sys.argv)
# print(args)
# print(f"{args.fahrenheit} Fahrenheit")

if args.verbose:
    print(str(args) + " It's verbose argument")
if args.fahrenheit and args.celsius:
    print("IT IS PROHIBITED!")
    quit()
if args.fahrenheit:
    # print(f"{args.fahrenheit} Fahrenheit in the logic")
    print(fahrenheit_to_celsius(args.fahrenheit))
if args.celsius:
    print(celsius_to_fahrenheit(args.celsius))
else:
    answer = str(input("What temperature you want convert?: ")).lower()

    while answer not in (CELSIUM_INPUT + FAH_INPUT + QUIT_INPUT):
        answer = str(input("What temperature you want convert?: ")).lower()

    if answer in QUIT_INPUT:
        quit()

    if answer in CELSIUM_INPUT:  # Convert from Celsius to Fahrenheit
        celsius = input("Provide temperature in Celsius: ")
        if is_float(celsius):
            print(celsius_to_fahrenheit(float(celsius)))
        else:
            print(f"ERROR: {celsius} is not convertible to float type")

    if answer in FAH_INPUT:  # Convert from Fahrenheit to Celsius
        fahrenheit = input("Provide temperature in Fahrenheit: ")
        if is_float(fahrenheit):
            print(fahrenheit_to_celsius(float(fahrenheit)))
        else:
            print(f"ERROR: {fahrenheit} is not convertible to float type")
