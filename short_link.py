import requests


url = input('URL: ')
response = requests.post('https://cleanuri.com/api/v1/shorten', data={'url': url}).json()
key = 'result_url'
if key in response:
    print(f'{key}: {response[key]}')
else:
    print('Invalid URL!')