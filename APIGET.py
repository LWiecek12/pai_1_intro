import requests

url = 'https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json'

try:
    response = requests.get(url)

    response.raise_for_status()

    print(response.json())

except requests.HTTPError as http_error:
    print(f'Błąd żądania HTTP: {http_error}')
except requests.RequestException as request_exception:
    print(f'Wystąpił błąd: {request_exception}')
