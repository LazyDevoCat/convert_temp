# -*- encoding: utf-8 -*-
import sys

from arguments import parse_arguments
from converter.converter import get_convertor_function
from converter.exception import TemperatureError, ConverterError
from converter.utils import is_float
from interactive import get_interactive_function, CELSIUM_INPUT, FAH_INPUT, QUIT_INPUT

args = parse_arguments()


if args.verbose:
    print(str(sys.argv) + " It's verbose argument")


def get_temperature(args) -> float:
    if args.temperature is None:
        raise ConverterError("Provide value for converting")
    return args.temperature


if args.fahrenheit or args.celsius:
    converter_function = get_convertor_function(args.fahrenheit, args.celsius)
    try:
        temperature = get_temperature(args)
        print(converter_function(temperature))
    except (TemperatureError, ConverterError) as error:
        print(f"{error}")
    quit()


answer = str(input("What temperature you want convert?: ")).lower()
while answer not in (CELSIUM_INPUT + FAH_INPUT + QUIT_INPUT):
    answer = str(input("What temperature you want convert?: ")).lower()


if answer in (CELSIUM_INPUT + FAH_INPUT):
    conversion_function, temperature = get_interactive_function(answer)
    if is_float(temperature):
        try:
            print(conversion_function(float(temperature)))
        except TemperatureError as error:
            print(f"{error}")
        quit()
    else:
        print(f"ERROR: {temperature} is not convertible to float type")


# if __name__ == '__main__':
