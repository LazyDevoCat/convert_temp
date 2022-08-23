
class TemperatureError(Exception):

    def __init__(self, temperature, absolute_zero):
        self.absolute_zero = absolute_zero
        self.temperature = temperature

    def __str__(self):
        return f"Temperature {self.temperature} should not be " \
               f"lower than absolute zero {self.absolute_zero}"


class ConverterError(Exception):
    pass
