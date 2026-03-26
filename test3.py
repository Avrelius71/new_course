import requests


response = requests.get('https://playground.learnqa.ru/api/long_redirect', allow_redirects=True)
first_response = response.history[0]
second_resp = response.history[1]
finel_response = response
print(first_response.url)
print(second_resp.url)
print(finel_response.url)
