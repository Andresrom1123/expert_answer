from rest_framework.test import APITestCase


class TestMyTokenObtainPairView(APITestCase):
    def setUp(self) -> None:
        self.url_base = 'http://127.0.0.1:8000/'
        url_user = f'{self.url_base}api/v1/users/'
        self.client.post(url_user, {'username': 'prueba', 'email': 'prueba@123.com', 'password': '123',
                                    'first_name': '123', 'last_name': '123'})

    def test_validate(self):
        url = f'{self.url_base}api/token/'
        response = self.client.post(url, {'email': 'prueba@123.com', 'password': '123'})
        self.assertEqual(response.data['username'], 'prueba')
        self.assertEqual(response.data['first_name'], '123')
        self.assertEqual(response.data['last_name'], '123')
        self.assertEqual(response.data['email'], 'prueba@123.com')
        self.assertEqual(response.data['token'], response.data['token'])
        self.assertEqual(response.data['refresh'], response.data['refresh'])
