# print, list, len, type, int, float, str, input, round, abs, min, max, sum, range, set, dict,enumerat

# print allows to print input of different data types
print('Asab', 250, True, ['HTML','CSS','JS'], 9.81, 3.14)

# type: allows to know the data type of the input
print(type(10))
print(type(9.81))
print(type(1 + 2j))
print(type(True))
print(type(False))
print(type(0 < 1))
print(type('10'))
print(type(int('10')))
print(type(str(10)))
print(type(9.81))
print(type('9.81'))
print(type(float('9.81')))
print(type([1, 2, 3]))
print(type((1, 2, 3)))
print(type({1, 2, 3}))
print(type({'name':'Asab', 'age':250}))

""" name = input('Enter a name: ')
birth_year = input('Enter birth year: ')
current_year = 2024 
age = current_year - int(birth_year)
print(age) """

mass = 74.54
gravity = 9.81 
weight = mass * gravity 
print(round(weight, 2))

print(abs(4), abs(-4))
print(min(10, -5, 20, -15, 40, 20))
print(max(10, -5, 20, -15, 40, 20))
print(sum([10, -5, 20, -15, 40, 20]))

print(list(range(0, 101, 1)))
print(list(range(1, 101, 1)))
print(list(range(0, 101, 2)))
print(list(range(1, 101, 2)))

""" print(list(range(0, 101, 5)))
print(list(range(0, 101, 10)))
print(list(range(-10000, 10001, 1)))
lst = list(range(-10000, 10001, 1))
print(len(lst)) """

lst = ['Finland','Sweden','Finland','Denmark','Finland','Sweden','Norway']
print(len(lst))
st = set(lst)
print(len(st))
print(list(enumerate(lst)))

for index, value in enumerate(lst):
    print(index + 1, value)
'''

I want you to use print with diffferent data types and share your code on the comment

'''
lst = [1, -500, 2, -1500, 20]
print(sum(lst))

print(list(range(0,202,2)))

print(max(10, -1, -2, -7, 20))

print(abs(3), abs(-10))

print (type((1, 2, 3)))
print (type([1, 2, 3]))
 