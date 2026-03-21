from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions


class TestUserDelete(BaseCase):
    # LOGIN
    def test_delete_undeletable_user(self):
        login_data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        response1 = MyRequests.post('/user/login', data=login_data)
        auth_sid = self.get_cookie(response1, 'auth_sid')
        token = self.get_header(response1, 'x-csrf-token')
        user_id = self.get_json_value(response1, 'user_id')

        response2 = MyRequests.delete(
            f'/user/{user_id}',
            cookies={'auth_sid': auth_sid},
            headers={'x-csrf-token':token}
        )
        Assertions.assert_status_code(response2, 400)
        assert response2.json()['error'] == 'Please, do not delete test users with ID 1, 2, 3, 4 or 5.'

    def test_delete_users(self):
        # REGISTER
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post('/user/', data=register_data)

        email = register_data['email']
        first_name = register_data['firstName']
        password = register_data['password']
        user_id = self.get_json_value(response1, 'id')

        # LOGIN
        login_data = {
            'email': email,
            'password': password
        }
        response2 = MyRequests.post('/user/login', data=login_data)

        auth_sid = self.get_cookie(response2, 'auth_sid')
        token = self.get_header(response2, 'x-csrf-token')

        response3 = MyRequests.delete(
            f'/user/{user_id}',
            cookies={'auth_sid': auth_sid},
            headers={'x-csrf-token': token}
        )
        Assertions.assert_status_code(response3, 200)

        response4 = MyRequests.get(
            f'/user/{user_id}',
            cookies={'auth_sid': auth_sid},
            headers={'x-csrf-token': token}
        )
        Assertions.assert_status_code(response4, 404)
        assert response4.content.decode('utf-8') == 'User not found'

    def test_delete_users_no_auth(self):
        # REGISTER
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post('/user/', data=register_data)

        email = register_data['email']
        first_name = register_data['firstName']
        password = register_data['password']
        user_id = self.get_json_value(response1, 'id')

        # LOGIN
        login_data = {
            'email': email,
            'password': password
        }
        response2 = MyRequests.post('/user/login', data=login_data)

        auth_sid = self.get_cookie(response2, 'auth_sid')
        token = self.get_header(response2, 'x-csrf-token')

        response3 = MyRequests.delete(
            '/user/10',
            cookies={'auth_sid': auth_sid},
            headers={'x-csrf-token': token}
        )
        Assertions.assert_status_code(response3, 400)
        assert response3.json()['error'] == 'This user can only delete their own account.'
