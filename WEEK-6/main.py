# import custom_modules
from custom_modules import add_two_nums, make_square, filter_country_by_starting_letter, change_list_upper
# from custom_modules import *
from countries_data import countries_data

# 'add_two_nums', 'change_list_upper', 'filter_country_by_starting_letter', 'make_square'
print(add_two_nums(2, 3))
print(make_square(10))
names = ['Artem', 'Carlos','Carina','Osuria','Maria', 'Lisandro','Ayong','Eir', 'Asabeneh']

countries = [country['name'] for country in countries_data]
print(change_list_upper(names))
print(filter_country_by_starting_letter('A', countries))