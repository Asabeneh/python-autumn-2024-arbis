
x = -10
if x > 0:
    print(f'{x} is a positive number')
elif x == 0:
    print(f'{x} is zero')
else:
    print(f'{x} is a negative number')
    

is_raining = False 

if is_raining:
    print('Take your umbrella with you')
else:
    print('Go out freely it seems a shinny day!')
    
""" 
weather = input('Enter the weather: ').lower()

if weather == 'rainy':
    print('Take your umbrella with you')
elif weather == 'sunny':
    print('Go out freely it seems a shinny day!')
elif weather == 'foggy':
    print('Be carefully, there might visibility')
elif weather == 'snowy':
    print('It could be slippery')
elif weather == 'cloudy':
    print('There is a high chance of rain')
else:
    print('No one knows the weather!') """
    
"""     
weather = input('Enter the weather: ').lower()
match weather:
    case 'rainy':
        print('Take your umbrella with you')
    case 'sunny':
        print('Go out freely it seems a shinny day!')
    case 'foggy':
        print('Be carefully, there might visibility')
    case 'snowy':
        print('It could be slippery')
    case 'cloudy':
        print('There is a high chance of rain')
    case _:
        print('No one knows the weather!') """
        
gender = 'Male'
pronoun =  'He' if gender == 'Male' else 'She'
print(pronoun)

