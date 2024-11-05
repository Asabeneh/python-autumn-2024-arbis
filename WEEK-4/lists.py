# List is a collection of ordered and indexed item
# List of names, countries, numbers, 

empty_lst = []
print(empty_lst, len(empty_lst), type(empty_lst))
print(dir(empty_lst))
# 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'

nums = [1, 2, 3, 4, 5]
print(len(nums))
print(nums[0])
print(nums[1])
print(nums[2])
last_index = len(nums) - 1
print(nums[last_index])
print(nums[-1])
print(nums[1:])
print(nums[3:])
print(nums[1:4])
print(nums[-4:-1])

nums[0] = 101
print(nums)
nums[-1] = 505
print(nums)
shopping_list = ['Milk','Coffee', 'Bread']
print(shopping_list)
print(len(shopping_list))
shopping_list.append('Honey')
print(shopping_list)
shopping_list.append('Potato')
print(shopping_list)
shopping_list.extend(['Tomato','Banana','Sugar', 'Onion','Orange'])
print(shopping_list)
# shopping_list.pop(3)
# shopping_list.remove('Sugar')
# del shopping_list[0]
print(shopping_list)
shopping_list.insert(6, 'Beans')
print(shopping_list)
# del shopping_list[4:]
print(shopping_list)
print(shopping_list.index('Milk'))
print('Pineaple' in shopping_list)

sentence = 'I love people, the love of people is killing me. love is such a great thing. Love is blind.'
print(sentence.count('love'))
words = sentence.lower().replace('.', ' ').split()
print(words, words.count('love'))

nums = [2, 3, 1, 4, 10]
nums_copy = nums.copy()
nums_copy.sort(reverse=False)
# nums_copy.reverse()
print(nums)
print(nums_copy)
nums = []
# nums.clear()
print(nums)

num1 = [1, 2, 3]
num2 = [4, 5, 6]
num3 = num1 + num2
print(num3)
nums4 = [0, *num1, *num2, 7, 8, 9, 10]
print(nums4)

countries = ['Netherlands','Germany','Belgium','France','Finland','Sweden','Norway','Denmark', 'Iceland']
ne, ge, _, fr, *northern_europe = countries
print(ne)
print(ge)
print(fr)
print(northern_europe)
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
min_age = ages[0]
max_age = ages[-1]
print(min_age, max_age)

