import requests
import pprint

# Задание 01

param = {
     'q':'html'
 }
response = requests.get('https://api.github.com/search/repositories', params=param)
print(f'Статус код: {response.status_code}')
response_json = response.json()
pprint.pprint(response_json)

# Задание 02

url = "https://jsonplaceholder.typicode.com/posts"

params = {"userid" : 1}

response = requests.get(url, params=params)
print(response.text)

#  Задание 03

data = {
    "title": "тестовый post запрос",
    "body" : "тестовый контент post запроса",
    "usrid" : 1
}

response = requests.post(url, data=data)
print(f'Статус-код : {response.status_code}')
print(response.text)

