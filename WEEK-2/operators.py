'''
Operators:
- Assignment operators =
- Arithmetic operators- +, -, *, /, %, //, **
- Comparison operators - >, >=, <, <=, ==, !=
- Logical operators: and, or, not

'''
# Assignment operator
a = 3
age = 250
print(a)
print(age)

# Arithmetic operator: +, -, *, /, %, //, **
print('additon:', 3 + 4)
print('subtraction', 4 - 3)
print('multiplication', 3 * 4)
print('division', 3 / 4)
print('remainder', 4 % 3) # 1
print('flooer divion',  9 // 5) # 1
print('exponentiation', 2 * 2 * 2, 2 ** 3, 2 ** 10)

'''
use modulos operator and print the value
use floor division operator and print the value with print function
use exponentiation operator and print the value with print function

'''
print(14 % 3) #2
print(14 // 3) #4
print(2 ** 2) #4

print('remainder', 5 % 3) #2
print('floor division', 13 // 5 ) #2
print('exponentiation', 1 * 15 + 3 - 2) #16

print(9 // 4) #2
print(3 ** 5) #243

print(25 % 5) # 0
print(25 // 3) #8
print(5 ** 3) #125

print('==== Comparison Operators =====')
 # Comparison: >, >=, <, <=, ==, !=

print(4 > 3)
print(4 >= 3)

print(3 < 4)
print(3 <= 4)

print(4 == 4)
print(4 == 3)
print(4 == '4')
print(4 == int('4'))
print(str(4) == '4')
print(4 != '4')
print(4 != 4)
print(True == True)
print(not True == False)

print(2 is 2)
print(2 is not 3)
print(2 in [1, 2, 3, 4])
print('land' in 'Finland')

# Logical Operators: and, or, not

print(4 > 3 and 3 < 4)
print(4 > 3 and 3 > 4)
print(4 < 3 and 3 > 4)

print(4 > 3 or 3 < 4)
print(4 > 3 or 3 > 4)
print(4 < 3 or 3 > 4)
print(True, not True, not False, not not True)
