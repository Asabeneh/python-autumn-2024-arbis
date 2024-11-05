# what are dictionaries: a structure way of storing data
# key value pair

fin_en_dict = {
    'auto':'car',
    'talo':'house',
    'tuoli':'chair',
    'kirja':'book'
}
print(fin_en_dict['auto'])
print(fin_en_dict['talo'])
print(fin_en_dict['tuoli'])

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'is_married':True,
    'skills':['HTML','CSS','JS','Python'],
    'height':1.72,
    'country':'Finland',
    'address': {
        'street_name':'Space street',
        'zipcode':'02270',
        'city':'Helsinki'
    }
}

print(person['first_name'])
print(person.get('first_name'))
print(person.get('nationality'))
if 'nationality' in person:
    print(person['nationality'])
else:
    person['nationality'] = 'Ethiopian'
print(person)

person['age'] = 50

print(person)

for key in person:
    print(key, person[key])
    
    
keys = person.keys()
print(keys)
values = person.values()
print(values)
items = person.items()
print(items)
for key, value in items:
    print(key, value)
    
empty_dict = dict() # {}
print(type(empty_dict), empty_dict)
print(len(person))
print(person['skills'])
person['skills'].append('MySQL')
print(person)
person['skills'].remove('JS')
print(person)

person.pop('age')
print(person)
del person['is_married']
print(person)

dog = {}
print(len(dog))
print(type(dog))
dog['color'] = 'black'
dog['age'] = 4
dog['breed'] = 'Husky'
print(dog)