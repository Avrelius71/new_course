import requests


methods = ['GET', 'POST', 'PUT', 'DELETE']
data = [
    {'method': 'GET'}, {'method': 'POST'}, {'method': 'PUT'}, {'method': 'DELETE'}
]

response1 = requests.get('https://playground.learnqa.ru/ajax/api/compare_query_type')
response2 = requests.head('https://playground.learnqa.ru/ajax/api/compare_query_type')
response3 = requests.get('https://playground.learnqa.ru/ajax/api/compare_query_type', params={'method': 'GET'})

print('респонс1')
print(response1.text)
print(response1.status_code)
print('респонс2')
print(response2.headers)
print(response2.status_code)
print('респонс3')
print(response3.text)
print(response3.status_code)

for param_value in data:
    for http_method in methods:

        if http_method == 'GET':
            response4 = requests.request(http_method, 'https://playground.learnqa.ru/ajax/api/compare_query_type', params=param_value)
        else:
            response4 = requests.request(http_method, 'https://playground.learnqa.ru/ajax/api/compare_query_type', data=param_value)

        print(f"Метод: {http_method}, Параметр: {param_value['method']}")
        print(f"Статус: {response4.status_code}")
        print(f"Ответ: {response4.text.strip()}")
        print('-' * 60)

