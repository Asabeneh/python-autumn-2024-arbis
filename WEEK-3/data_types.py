'''
- Data Types:  

- Numbers(int, float, complex)
- Strings
- Booleans(True or False)
- List
- Set
- Tuple
- Dictionary
'''

# Numbers (int, float, complex)

# integers
print(type(10))
print(type(100))
print(type(50))
print(type(-10))
print(type(0))

# floats

print(type(3.14))
print(type(9.81))
print(type(2.777))

# Complexnumbers

print(type(1 + 2j))
print(type(0 + 1j))
print(type(-5-5j))

# Booleans (True or False)
print(type(True))
print(type(False))
print(type(1 > 0))
print(type(1 == '1'))

# Strings: anything under sinqle, double or triple quote

print('a')
print(type('a'))
print('My students really love Python programming')
print('My students really love Python programming'.split())
print('water' + 'melon')
print('Asabeneh' + ' ' + 'Yetayeh')
print(len('Finland'))
print('land' in 'Finland')
print('Finland'.startswith('F'))
print('Finland'.endswith('d'))

# List: an ordered, indexed and can be mutated
print(type([]), [], list(), list('cat'))
print([0, 2, 4, 6, 8],len([0, 2, 4, 6, 8]))
print(['Finland','Sweden','Norway','Denmark','Iceland'])

# Set: No order and not indexed,does not allow duplicates
print(type(set()))
print({'Finland','Sweden','Norway','Denmark','Iceland', 'Finland', 'Iceland','Norway'})
print(list({'Finland','Sweden','Norway','Denmark','Iceland', 'Finland', 'Iceland','Norway'}))

# Tuple: indexed, ordered but immutable
print(type(()), (),  tuple(), ('Finland','Sweden','Norway','Denmark','Iceland'))

# Dictionaries: Key value pair 
print({
    'talo':'house',
    'auto':'car',
    'kirja':'book',
    'kirjasto':'library'
})
print({
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'country':'Finland',
    'city':'Helsinki',
    'age':250,
    'is_married':True,
    'skills':['HTML','CSS','JS','Python']
})