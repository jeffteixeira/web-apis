import requests


cep = input('CEP: ')
url = f'https://cep.awesomeapi.com.br/json/{cep}'
response = requests.get(url).json()
if response:
    for key in response:
        print(f'{key}: {response[key]}')
else:
    print('CEP not found!')