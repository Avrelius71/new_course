import pytest
import requests


test_data = [
    {
        'ua': 'Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
        'expected': {'platform': 'Mobile', 'browser': 'No', 'device': 'Android'}
    },
    {
        'ua': 'Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1',
        'expected': {'platform': 'Mobile', 'browser': 'Chrome', 'device': 'iOS'}
    },
    {
        'ua': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
        'expected': {'platform': 'Googlebot', 'browser': 'Unknown', 'device': 'Unknown'}
    },
    {
        'ua': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0',
        'expected': {'platform': 'Web', 'browser': 'Chrome', 'device': 'No'}
    },
    {
        'ua': 'Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
        'expected': {'platform': 'Mobile', 'browser': 'No', 'device': 'iPhone'}
    },
]

errors = []


@pytest.mark.parametrize('data', test_data)
def test_user_agent(data):
    url = "https://playground.learnqa.ru/ajax/api/user_agent_check"
    response = requests.get(url, headers={"User-Agent": data['ua']})
    result = response.json()
    expected = data['expected']

    for key in ['platform', 'browser', 'device']:
        if result.get(key) != expected[key]:
            errors.append({
                'ua': data['ua'][:80] + '...',
                'field': key,
                'expected': expected[key],
                'actual': result.get(key)
            })
            assert False, f"Поле '{key}': ожидал '{expected[key]}', получил '{result.get(key)}'"


def test_show_errors():
    if errors:
        print("\nНайдены ошибки:")
        for e in errors:
            print(f"  • {e['field']}: '{e['expected']}' ≠ '{e['actual']}' в {e['ua']}")
    else:
        print("\nВсе тесты прошли!")