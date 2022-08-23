from converter.converter import celsius_to_fahrenheit, fahrenheit_to_celsius

CELSIUM_INPUT = ['celsius', 'cels', 'cel', '-c', 'c']
FAH_INPUT = ['fahrenheit', 'fahren', 'far', '-f', 'f']
QUIT_INPUT = ['quit', 'q', 'exit']


def get_interactive_function(answer: str) -> tuple:
    if answer in QUIT_INPUT:
        quit()
    if answer in CELSIUM_INPUT:
        return celsius_to_fahrenheit, \
               input("Provide temperature in Celsius: ")

    if answer in FAH_INPUT:
        return fahrenheit_to_celsius, \
               input("Provide temperature in Fahrenheit: ")
    raise ValueError("Provide correct scale")
