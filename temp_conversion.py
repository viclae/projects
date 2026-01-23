def celsiustofahrenheit():
    while True:
        celsius = input('\nPlease input the temperature you would like to have converted (C): ').strip()
        try:
            celsius = float(celsius)
            break
        except ValueError:
            print('Please input a valid number (decimals and negatives are okay).')

    fahrenheit = round(celsius * (9/5) + 32, 1)
    print(f'\nThis temperature in Fahrenheit is {fahrenheit} degrees.')

def celsiustokelvin():
    while True:
        celsius = input('\nPlease input the temperature you would like to have converted (C): ').strip()
        try:
            celsius = float(celsius)
            break
        except ValueError:
            print('Please input a valid number (decimals and negatives are okay).')

    kelvin = round(celsius + 273.15, 1)
    print(f'\nThis temperature in Kelvin is {kelvin} degrees.')

def fahrenheittocelsius():
    while True:
        fahrenheit = input('\nPlease input the temperature you would like to have converted (F): ').strip()
        try:
            fahrenheit = float(fahrenheit)
            break
        except ValueError:
            print('Please input a valid number (decimals and negatives are okay).')

    celsius = round((fahrenheit - 32) * (5/9), 1)
    print(f'\nThis temperature in Celsius is {celsius} degrees.')

def fahrenheittokelvin():
    while True:
        fahrenheit = input('\nPlease input the temperature you would like to have converted (F): ').strip()
        try:
            fahrenheit = float(fahrenheit)
            break
        except ValueError:
            print('Please input a valid number (decimals and negatives are okay).')

    kelvin = round((fahrenheit + 459.67) * (5/9), 1)
    print(f'\nThis temperature in Kelvin is {kelvin} degrees.')

def kelvintocelsius():
    while True:
        kelvin = input('\nPlease input the temperature you would like to have converted (K): ').strip()
        try:
            kelvin = float(kelvin)
            break
        except ValueError:
            print('Please input a valid number (decimals and negatives are okay).')

    celsius = round(kelvin - 273.15, 1)
    print(f'\nThis temperature in Celsius is {celsius} degrees.')

def kelvintofahrenheit():
    while True:
        kelvin = input('\nPlease input the temperature you would like to have converted (K): ').strip()
        try:
            kelvin = float(kelvin)
            break
        except ValueError:
            print('Please input a valid number (decimals and negatives are okay).')

    fahrenheit = round(kelvin * (9/5) - 459.67, 1)
    print(f'\nThis temperature in Kelvin is {fahrenheit} degrees.')

def main():
    print('\nTemperature Converter')
    print('\n1. Celsius Converter'
          '\n2. Fahrenheit Converter'
          '\n3. Kelvin Converter')

    while True:
        choice = input('\nPlease choose one of the options above (1-3): ').strip()
        if not choice.isdigit():
            print('Please choose a valid integer.')
            continue

        choice = int(choice)

        if choice not in range(1, 4):
            print('Please choose a valid number between 1 and 3.')
            continue

        break

    if choice == 1:
        print('\n1. Celsius to Fahrenheit'
              '\n2. Celsius to Kelvin')

        while True:
            celsius_choice = input('\nPlease choose the temperature scale you would like to convert to from the options above: ').strip()
            if not celsius_choice.isdigit():
                print('Please choose a valid integer.')
                continue

            celsius_choice = int(celsius_choice)

            if celsius_choice not in range(1, 3):
                print('Please choose a valid number between 1 and 2.')
                continue

            break

        if celsius_choice == 1:
            celsiustofahrenheit()
        elif celsius_choice == 2:
            celsiustokelvin()

    if choice == 2:
        print('\n1. Fahrenheit to Celsius'
              '\n2. Fahrenheit to Kelvin')

        while True:
            fahrenheit_choice = input('\nPlease choose the temperature scale you would like to convert to from the options above: ').strip()
            if not fahrenheit_choice.isdigit():
                print('Please choose a valid integer.')
                continue

            fahrenheit_choice = int(fahrenheit_choice)

            if fahrenheit_choice not in range(1, 3):
                print('Please choose a valid number between 1 and 2.')
                continue

            break

        if fahrenheit_choice == 1:
            fahrenheittocelsius()
        elif fahrenheit_choice == 2:
            fahrenheittokelvin()

    if choice == 3:
        print('\n1. Kelvin to Celsius'
              '\n2. Kelvin to Fahrenheit')

        while True:
            kelvin_choice = input('\nPlease choose the temperature scale you would like to convert to from the options above: ').strip()
            if not kelvin_choice.isdigit():
                print('Please choose a valid integer.')
                continue

            kelvin_choice = int(kelvin_choice)

            if kelvin_choice not in range(1, 3):
                print('Please choose a valid number between 1 and 2.')
                continue

            break

        if kelvin_choice == 1:
            kelvintocelsius()
        elif kelvin_choice == 2:
            kelvintofahrenheit()

if __name__ == "__main__":
    main()