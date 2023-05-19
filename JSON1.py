import requests
import json

url = 'https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    members = data['members']

    print("Imiona członków zespołu super bohaterów:")
    for member in members:
        print(member['name'])
else:
    print("Wystąpił problem podczas pobierania danych. Kod odpowiedzi:", response.status_code)
