# What is string? 
# A textual data type
# How long is a string? A string could be just only one character or several pages of text
# how to create a string? A string can be created using single, double or triple quote

empty_string = ''
print(len(empty_string), type(empty_string))
letter = 'a' # a string of one character
print(len(letter))
word = 'Love' 
print(word)
print(len(word))
sentence = 'I love people. People are great.'
print(len(sentence))

print(word.upper())
print(word.lower())
print(word.replace('o','0'))
print(list(word))

print(sentence)
print(sentence.lower().replace('.', ' ').split())
words = sentence.lower().replace('.', ' ').split()
print(words, len(words))
print(set(words), len(set(words)))

print(sentence.lower())
print(sentence.upper())
print(sentence.title())
print(sentence.swapcase())

print(sentence.startswith('I love'))
print('love' in sentence)
print(sentence.endswith('great'))

country = 'Finland2024'
print(country.islower())
print(country.isupper())
print(country.isalpha())
print(country.isalnum())
print(country.isdigit())

multiline_string = '''I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python.'''

first_name = 'Asabeneh'
last_name = 'Yetayeh'
age = 250 
country = 'Finland'
city = 'Helsinki'
full_name = first_name + ' ' + last_name
print(full_name)
print('I am ' + full_name + '.' + ' I am ' + str(age) + ' years old.' + 'I based in ' + city + ', ' + country + ' .')
# print(f'I am {full_name}. I am {age}  years old. I based in {city}, {country}.')
print(f'I am {full_name}. I am {age} years old. I based in  {city}, {country}.')
print(f'I am {full_name}.\nI am {age} years old.\nI based in  {city}, {country}.')

print('Name\t\tCountry\t\tAge')
print(f'{first_name}\t\t{country}\t\t{age}')

print('I hope everyone is enjoying the Python Challenge.\nAre you ?') # line break
print('Days\tTopics\tExercises') # adding tab space or 4 spaces 
print('Day 1\t5\t5')
print('Day 2\t6\t20')
print('Day 3\t5\t23')
print('Day 4\t1\t35')

print('The slash(\\) allow us \\ to escape the default behavior')
print("The cliche that goes \'an apple a day keep the doctor away\' ")
print('The cliche that goes \"an apple a day keep the doctor away\"')

# Strings only
first_name = 'Asabeneh'
last_name = 'Yetayeh'
language = 'Python'
age = 250
height = 1.72
formated_string = 'I am %s %s. I teach %s. I am %d years old. I am %.2f meter tall.' %(first_name, last_name, language, age, height)
print(formated_string)

formated_string = 'I am {} {}. I teach {}. I am {} years old. I am {} meter tall.'.format(first_name, last_name, language, age, height)
print(formated_string)

formated_string = f'I am {first_name} {last_name}. I teach {language}. I am {age} years old. I am {height} meter tall.'
print(formated_string)

language = 'Python'
one,two,c,d,_,f = language # unpacking sequence characters into variables
print(one) # P
print(two) # y
print(c) # t
print(d) # h

print(f) # n
print(language)
print(language[0])
print(language[1])
print(language[2])
last_index = len(language) - 1
print(language[last_index])
print(language[-1])

print(language)
print(language[1:6])
print(language[1:])
print(language[2:5])
print(language[::])
print(language[::-1])
# it is good for checking a palindrome: eg.civic, radar, level, rotor, kayak, madam, and refer
print('civic' == 'civic'[::-1])
print('car' == 'car'[::-1])
print(language[0:6:1])

challenge = 'thirty\tdays\tof\tpython'
print(challenge)
print(challenge.expandtabs())   # 'thirty  days    of      python'
print(challenge.expandtabs(10)) # 'thirty    days      of        python'
print(challenge.expandtabs(20)) # 'thirty    days      of        python'

challenge = 'thirty days of python'
sub_string = 'on'
print(challenge.index(sub_string))  # 7
print(challenge.index(sub_string, 8)) # error

challenge = '\u00B2'
print(challenge.isdigit())  
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
print(', '.join(web_tech))

txt = '    i love people   '
print(txt)
print(txt.strip())
    
