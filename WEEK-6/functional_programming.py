# map, filter, reduce

# [1, 2, 3, 4, 5] => [11, 12, 13, 14, 15]
# ['Finland', 'Sweden','Norway', 'Denmark', 'Iceland'] => ['FIN', 'SWE', 'NOR', 'DEN, 'ICE]
from pprint import pprint
nums = [1, 2, 3, 4, 5]

def square(lst):
    new_lst = []
    for num in lst:
        new_lst.append(num  ** 2)
    return new_lst
    
print(square(nums))
    
countries = ['Finland', 'Sweden','Norway', 'Denmark', 'Iceland'] 
counry_codes = []
for country in countries:
    counry_codes.append(country.upper()[:3])
print(counry_codes)

def double_num (x):
    return x * 2

squares = list(map(lambda x: x ** 2, nums))
print(squares)

country_codes = list(map(lambda country: country.upper()[:3], countries))
print(counry_codes)
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]

def create_country_codes(lst):
    return list(map(lambda country: country.upper()[:3], lst))

print(create_country_codes(countries))
pprint(list(map(lambda country:[country, len(country), country.upper()[:3]], countries)))

nums = [-3, 5, 2, 1, 0, -2, 4, -8]

evens = []
for num in nums:
    if num % 2 == 0:
        evens.append(num)
print(evens)

positive_evens = []
for num in nums:
    if num % 2 == 0 and num > 0:
        positive_evens.append(num)
print(positive_evens)

evens = list(filter(lambda num: num % 2 == 0, nums))
print(evens)

odds = list(filter(lambda num: num % 2 != 0, nums))
print(odds)

countries_with_land = list(filter(lambda country: 'land' in country, countries))
pprint(countries_with_land)
countries_endswith_stan = list(filter(lambda country: country.endswith('stan'), countries))
pprint(countries_endswith_stan)

print(list(filter(lambda country: len(country.split()) > 2, countries)))

from functools import reduce 

nums = [1, 2, 3, 4, 5]
total = 0 
for num in nums:
    total += num 
print(total)

print(reduce(lambda acc, cur: acc + cur, nums, 0))
from countries_data import countries_data

# pprint(countries_data)
# pprint(list(map(lambda country: [country['name'], country['capital'], country['population']], countries_data)))
world_population = reduce(lambda acc, cur: acc + cur['population'], countries_data, 0)
print(f'{world_population:,}')