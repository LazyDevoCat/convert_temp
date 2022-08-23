import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Take temperature in Fahrenheit(Celsius) "
                    "and convert to Celsius(Fahrenheit)"
    )

    parser.add_argument(
        "-v", "--verbose", help="It just return your argument"
    )

    parser.add_argument(
        "temperature", type=float,
        help="temperature", action="store", nargs='?'
    )

    scale_group = parser.add_mutually_exclusive_group(required=False)

    scale_group.add_argument(
        "-f", "--fahrenheit", action="store_true",
        help="use flag -f(--fahrenheit) and provide one value for converting"
    )

    scale_group.add_argument(
        "-c", "--celsius", action="store_true",
        help="use flag -c(--celsius) and provide one value for converting"
    )

    return parser.parse_args()
