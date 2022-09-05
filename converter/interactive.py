from converter.converter import celsius_to_fahrenheit, fahrenheit_to_celsius, ConverterContext
from converter.utils import is_float

CELSIUS_INPUT = ['celsius', 'cels', 'cel', '-c', 'c']
FAH_INPUT = ['fahrenheit', 'fahren', 'far', '-f', 'f']
QUIT_INPUT = ['quit', 'q', 'exit']


class InteractiveContext(ConverterContext):
    def get_converter(self):
        answer = str(input("What temperature you want convert?: ")).lower()
        while answer not in (CELSIUS_INPUT + FAH_INPUT + QUIT_INPUT):
            answer = str(input("What temperature you want convert?: ")).lower()

        if answer in QUIT_INPUT:
            quit()
        if answer in CELSIUS_INPUT:
            return celsius_to_fahrenheit

        if answer in FAH_INPUT:
            return fahrenheit_to_celsius
        raise ValueError("Provide correct scale")

    def get_temperature(self):
        temperature = input("Provide temperature: ")
        if not is_float(temperature):
            raise ValueError(f"ERROR: {temperature} is not convertible to float type")
        return float(temperature)
