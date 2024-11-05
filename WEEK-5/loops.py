
# What is a loop: it a block of code that allows to solve repetive problem

for i in range(1, 101):
    print(f'{i}  - Hello World!')
    

names = ['Artem', 'Carlos','Carina','Osuria','Maria', 'Lisandro','Ayong','Eir', 'Asabeneh']

for name in names:
    if len(name) < 6:
        print(f'{name} is a short name.')
        
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


countries_with_land = []

for country in countries:
    # print(country, country.upper(), len(country))
    if 'land' in country:
        countries_with_land.append(country)
print(countries_with_land)

for index, name in enumerate(countries):
    print(f'{index  + 1} - {name}')
    
total = 0
for i in range(101):
    total = total + i 
print(total)


for i in range(100, -1, -1):
    print(i)
    
    
for _ in range(10):
    print('do the operation 10x')

print(names)
for i in range(len(names)):
    print(names[i])
    

for name in names:
    print(names)
    
    
nums = [0, -5, 2, 3, -4, 4, 6, -3, 0, 8]

total = 0 
for num in nums:
    total = total + num 

print(total)

positive_nums = []
for num in nums:
    if num > 0:
        positive_nums.append(num)
print(positive_nums)
        
        
negative_nums = []
for num in nums:
    if num < 0:
        negative_nums.append(num)
print(negative_nums)
        
    
even_nums = []
for num in nums:
    if num % 2 == 0 and num > 0:
        even_nums.append(num)
print(even_nums)

for num in nums:
    if num < 0:
        break 
    print(num)
    
for num in nums:
    if num < 0:
        continue
    print(num)
        
        
    # While loop
    
count = 0 

while count <= 10:
    print(count)
    count = count + 1
    

count = 5

while count >= 0:
    print(count)
    count = count - 1
    
    
names = []

while True:
    name = input('Enter name: ')
    if name == '' or name == 'quit':
        break
    names.append(name)
print(names)
    
    