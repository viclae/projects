print('\nBMI Calculator')

def bmi_calculator():
    while True:
        try:
            weight = float(input('\nWeight in kilograms: '))
            height = float(input('Height in meters: '))

            if weight <= 0 or height <= 0:
                print('Weight and height must be higher than 0.')
                continue

            bmi = weight / (height**2)
            str(bmi)

            print(f'\nBMI: {bmi:.2f}')

            if bmi < 18.5:
                category = 'underweight'
            elif bmi >= 18.5 and bmi < 25:
                category = 'normal weight'
            elif bmi >= 25 and bmi < 30:
                category = 'overweight'
            elif bmi >= 30:
                category = 'obese'
            
            print(f'You are {category}.')
            break

        except ValueError:
            print('Invalid input! Please enter numbers only.')

bmi_calculator()