import requests
import json

url = 'https://httpbin.org/post'
headers = {'Content-Type': 'application/json'}
data = {'name': 'natalia'}

try:
    response = requests.post(url, headers=headers, data=json.dumps(data))

    response.raise_for_status()

    print(response.json())

except requests.HTTPError as http_error:
    print(f'Błąd żądania HTTP: {http_error}')
except requests.RequestException as request_exception:
    print(f'Wystąpił błąd: {request_exception}')
