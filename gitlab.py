import requests


username = input('Username: ')
url = f'https://gitlab.com/api/v4/users?username={username}'
response = requests.get(url).json()
if response:
    data = response[0]
    for key in data:
        print(f'{key}: {data[key]}')
else:
    print('Username not found!')
