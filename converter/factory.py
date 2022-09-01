from converter.arguments import ArgumentContext, parse_arguments
from converter.converter import ConverterContext
from converter.interactive import InteractiveContext


class ConvertorContextFactory(object):

    def create(self) -> ConverterContext:
        if self.has_necessary_arguments():
            return ArgumentContext()
        else:
            return InteractiveContext()

    def has_necessary_arguments(self) -> bool:
        argument = parse_arguments()
        return argument.temperature is not None and (argument.fahrenheit or argument.celsius)
