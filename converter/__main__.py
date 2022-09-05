# -*- encoding: utf-8 -*-

from converter.exception import TemperatureError, ConverterError
from converter.factory import ConverterContextFactory

converter_context = ConverterContextFactory().create()
try:
    converter = converter_context.get_converter()
    temperature = converter_context.get_temperature()
    print(converter(temperature))
except (TemperatureError, ConverterError, ValueError) as error:
    print(f"{error}")
