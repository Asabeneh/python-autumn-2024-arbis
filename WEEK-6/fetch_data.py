import requests
from pprint import pprint

def fetch_data(url):
    import requests
    response = requests.get(url)
    data = response.json()
    return data
    


url = 'https://api.thecatapi.com/v1/breeds'
data = fetch_data(url)
print('Number of breeds: ', len(data))
# pprint(data[0])

cats = [
    {
        'name':cat['name'], 
        'country':cat['origin'], 
        'description':cat['description'],
        'weight':cat['weight']['metric'],
        'life_span':cat['life_span'],
        'reference_image_id':cat.get('reference_image_id')
        } for cat in data ]
pprint(cats)

