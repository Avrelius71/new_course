import requests
import pytest


def test_headers():
    response = requests.get('https://playground.learnqa.ru/api/homework_header')
    print(response.headers)
    headers = response.headers.get('x-secret-homework-header')
    assert headers == 'Some secret value'


