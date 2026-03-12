import requests


methods = ['GET', 'POST', 'PUT', 'DELETE']
data = [
    {'method': 'GET'}, {'method': 'POST'}, {'method': 'PUT'}, {'method': 'DELETE'}
]

response1 = requests.get('https://playground.learnqa.ru/ajax/api/compare_query_type')
response2 = requests.head('https://playground.learnqa.ru/ajax/api/compare_query_type')
response3 = requests.get('https://playground.learnqa.ru/ajax/api/compare_query_type', params='GET')

print('респонс1')
print(response1.text)
print(response1.status_code)
print('респонс2')
print(response2.text)
print(response2.status_code)
print('респонс3')
print(response3.text)
print(response3.status_code)

for i in data:
    response4 = requests.post('https://playground.learnqa.ru/ajax/api/compare_query_type', data=i)
    print(i)
    print(response4.text)
    print(response4.status_code)

