# List comprehension: allow us to write a compact code
# performant and takes less memory
from countries_data import countries_data
from pprint import pprint
countries = ['Finland', 'Sweden','Norway', 'Denmark', 'Iceland']
country_codes = [country.upper()[:3] for country in countries]
print(country_codes)
populations = [country['population'] for country in countries_data]
world_population = sum(populations)
print(f'{world_population:,}')

# print([country['population'] for country in countries_data])

country_capital_population = [[country['name'], country['capital'], country['population']] for country in countries_data]
pprint(country_capital_population )

pprint([country['name'] for country in countries_data if 'land' in country['name']])

nums =[[1, 2, 3], [4, 5, 6], [8, 9, 10]]
""" new_lst = []
for l in nums:
    new_lst.extend(l)
print(new_lst) """

print([num for lst in nums for num in lst])