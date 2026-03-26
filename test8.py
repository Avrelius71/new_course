import requests
import pytest


def test_cookies():
    response = requests.get('https://playground.learnqa.ru/api/homework_cookie')
    print(dict(response.cookies))
    cook = dict(response.cookies)
    assert 'HomeWork' in cook
    assert cook['HomeWork'] == 'hw_value'
