# -*- encoding: utf-8 -*-

from converter.exception import TemperatureError, ConverterError
from converter.factory import ConvertorContextFactory

converter_context = ConvertorContextFactory().create()
converter_function = converter_context.get_converter_function()
try:
    temperature = converter_context.get_temperature()
    print(converter_function(temperature))
except (TemperatureError, ConverterError, ValueError) as error:
    print(f"{error}")
