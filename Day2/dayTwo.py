temp = float(input('Enter the current temperature in fahrenheit:'))
print('Is it raining?')
print('1. yes')
print('2. no')

choice = int(input('choose yes or no:'))

def suggest_wear(temp,choice):
    if temp < 50 :
        print('You need to wear a coat, hat, scarf, and gloves.')

    elif temp > 50 and temp < 70 and choice == 2:
        print('You need to wear a sweater or light jacket.')

    elif temp > 50 and temp < 70 and choice == 1:
        print('You need to wear a rain jacket and boots.')

    elif temp > 70 and choice == 2:
        print('You need to wear a t-shirt and shorts.')

    elif temp > 70 and choice == 1:
        print('You need to wear a light jacket and rain boots.')
    
    else:
        print("invalid choice")


suggest_wear(temp,choice)