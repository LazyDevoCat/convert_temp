# -*- encoding: utf-8 -*-

from converter.exception import TemperatureError, ConverterError
from converter.factory import ConverterContextFactory

converter_context = ConverterContextFactory().create()
#converter_function = converter_context.get_converter()
try:
    temperature = converter_context.get_temperature()
    print(converter_context.get_converter()(temperature))
except (TemperatureError, ConverterError, ValueError) as error:
    print(f"{error}")
