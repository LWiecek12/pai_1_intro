import requests
import json

from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry


url = 'https://httpbin.org/delay/2'
headers = {'Content-Type': 'application/json'}
data = {'name': 'natalia'}

session = requests.Session()
retry_strategy = Retry(total=3, backoff_factor=1, status_forcelist=[429, 500, 502, 503, 504])
adapter = HTTPAdapter(max_retries=retry_strategy)
session.mount('https://', adapter)

try:
    response = session.post(url, headers=headers, data=json.dumps(data), timeout=1)

    response.raise_for_status()

    print(response.json())

except requests.HTTPError as http_error:
    print(f'Błąd żądania HTTP: {http_error}')
except requests.RequestException as request_exception:
    print(f'Wystąpił błąd: {request_exception}')
