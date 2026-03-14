import requests


payload = {'login': 'super_admin', 'password': 'welcome'}
response1 = requests.post('https://playground.learnqa.ru/ajax/api/get_secret_password_homework', data=payload)
cookie_value = response1.cookies.get('auth_cookie')
cookies = {'auth_cookie': cookie_value}

response2 = requests.post('https://playground.learnqa.ru/ajax/api/check_auth_cookie', cookies=cookies)
if response2.text == 'You are NOT authorized':
    print(response2.text)
else:
    print(response2.text)
    print(payload['password'])