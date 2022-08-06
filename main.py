import argparse


CELSIUM_INPUT = ['celsius', 'cels', 'cel', '-c', 'c']
FAH_INPUT = ['fahrenheit', 'fahren', 'far', '-f', 'f']
QUIT_INPUT = ['quit', 'q']


def cel_to_fahren(tempreture_in_celsium):
    """
    Take temperature in Celsius and convert to Fahrenheit
    Temp: 20 C
    20 * (9/5) + 32 = 68 F
    """
    fahren = (tempreture_in_celsium * (9 / 5)) + 32
    return fahren


def fahren_to_cel(temprutere_in_fahren):
    """
    Take temperature in Fahrenheit and convert to Celsius 
    Temp: 68 F
    (5/9) * (68 - 32) = 20 C
    """
    cels = (5 / 9) * (temprutere_in_fahren - 32)
    return cels


parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", help="It just return your argument")
parser.add_argument("-f", "--fahrenheit", help="Take temperature in Fahrenheit and convert to Celsius", type=float)
parser.add_argument("-c", "--celsius", help="Take temperature in Celsius and convert to Fahrenheit", type=float)

args = parser.parse_args()

if args.verbose:
    print(str(args) + " It's verbose argument")
elif args.fahrenheit:
    # print(f"{args.fahrenheit} Fahrenheit")
    print(fahren_to_cel(args.fahrenheit))
elif args.celsius:
    # print(f"{args.celsius} Celsius")
    print(cel_to_fahren(args.celsius))
else:
    answer = str(input("What teamprute you want convert?: ")).lower()

    while answer not in (CELSIUM_INPUT + FAH_INPUT):
        answer = str(input("What teamprute you want convert?: ")).lower()
        if answer in QUIT_INPUT:
            break

    if answer in CELSIUM_INPUT:  # Convert from Celsius to Fahrenheit
        celsium = float(input("Provide tempruture in Celsius: "))
        print(cel_to_fahren(celsium))

    if answer in FAH_INPUT:  # Convert from Fahrenheit to Celsius
        fahrenheit = float(input("Provide tempruture in Fahrenheit: "))
        print(fahren_to_cel(fahrenheit))
