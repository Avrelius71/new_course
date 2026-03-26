import requests
import time


response1 = requests.get('https://playground.learnqa.ru/ajax/api/longtime_job')
token_values = response1.json()['token']
times = response1.json()['seconds']
token = {'token': token_values}
response2 = requests.get('https://playground.learnqa.ru/ajax/api/longtime_job', params=token)
print(response2.text)
if response2.json()['status'] == 'Job is NOT ready':
    print('Задача еще не выполнена, статус корректный')
print(f'Ждем {times} сек')
time.sleep(times)
response3 = requests.get('https://playground.learnqa.ru/ajax/api/longtime_job', params=token)
print(response3.text)
if 'result' in response3.json() and response3.json()['status'] == 'Job is ready':
    print('поле result присутствует, статус корректный')