def abc():
    print('I am learning my abc')
    
abc()

def add_two_nums(a, b):
    return a + b 
 

print(add_two_nums(10, 90))

def make_square(x):
    return x ** 2

print(make_square(10))

square = lambda x: x * x

print(square(3))

add_three_nums = lambda a, b, c : a + b + c

print(add_three_nums(20, 30, 40))

'''
write a lambda function that has three parameter such as x, y , c

y - 2 * x + c

Evaluate for the value 8, 3, 1


'''

linear_eqn = lambda x, y, c : y - 2 * x + c
print(linear_eqn(3, 8, 1))