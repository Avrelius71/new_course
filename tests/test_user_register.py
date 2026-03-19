from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions
import pytest


class TestUserRegister(BaseCase):
    negative_data = [
        ({'username': 'learnqa', 'firstName': 'lear', 'lastName': 'learnqa', 'email': 'vin@example.com'}, 'password'),
        ({'password': '123', 'firstName': 'lear', 'lastName': 'learnqa', 'email': 'vin@example.com'}, 'username'),
        ({'password': '123', 'username': 'lear', 'lastName': 'learnqa', 'email': 'vin@example.com'}, 'firstName'),
        ({'password': '123', 'username': 'lear', 'firstName': 'learnqa', 'email': 'vin@example.com'}, 'lastName'),
        ({'password': '123', 'username': 'lear', 'firstName': 'learnqa', 'lastName': 'learnqa'}, 'email')
    ]
    negative_data_long_firstname = {
        'firstName': 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor.'
                     ' Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus'
                     ' mus. Donec quam felis, ultricies nec, pellentesque eu, pretium q',
        'password': '123', 'username': 'learnqa', 'lastName': 'learnqa', 'email': 'vin@example.com'
    }

    negative_data_short_firstname = {'password': '123', 'username': 'learnqa', 'firstName': 'l',
                                     'lastName': 'learnqa', 'email': 'vin@example.com'}

    def test_create_user_successfully(self):
        data = self.prepare_registration_data()
        response = MyRequests.post('/user/', data=data)
        Assertions.assert_status_code(response, 200)
        Assertions.assert_json_has_key(response, 'id')

    def test_negative_format_email(self):
        email = 'vinkotovexample.com'
        data = self.prepare_registration_data(email)
        response = MyRequests.post('/user/', data=data)
        Assertions.assert_status_code(response,400)
        assert response.content.decode('utf-8') == f"Invalid email format"

    def test_negative_registration_long_firstname(self):
        data = self.negative_data_long_firstname
        response = MyRequests.post('/user/', data=data)
        Assertions.assert_status_code(response,400)
        assert response.content.decode('utf-8') == f"The value of 'firstName' field is too long"

    def test_negative_registration_short_firstname(self):
        data = self.negative_data_short_firstname
        response = MyRequests.post('/user/', data=data)
        Assertions.assert_status_code(response,400)
        assert response.content.decode('utf-8') == f"The value of 'firstName' field is too short"

    @pytest.mark.parametrize('data, expected_error', negative_data)
    def test_negative_registration(self, data, expected_error):
        response = MyRequests.post('/user/', data=data)
        Assertions.assert_status_code(response, 400)
        assert response.content.decode('utf-8') == f"The following required params are missed: {expected_error}"

    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data = self.prepare_registration_data(email)
        response = MyRequests.post('/user/', data=data)
        Assertions.assert_status_code(response, 400)
        assert response.content.decode('utf-8') == f"Users with email '{email}' already exists"

