# -*- encoding: utf-8 -*-
import sys

from .converter import ConverterContext
from .exception import TemperatureError, ConverterError

converter_context = ConverterContext()


# args = parse_arguments()
# if args.verbose:
#     print(str(sys.argv) + " It's verbose argument")

converter_function = converter_context.get_converter_function()
try:
    temperature = converter_context.get_temperature()
    print(converter_function(temperature))
except (TemperatureError, ConverterError) as error:
    print(f"{error}")
quit()

