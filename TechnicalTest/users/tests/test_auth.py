"""Auth tests."""

# Django
from django.test import TestCase

# Django REST Framework
from rest_framework import status
from rest_framework.test import APITestCase

# Model
from users.models import User
from users.authentication import BearerAuthentication
from rest_framework.authtoken.models import Token




class AuthAPITestCase(APITestCase):
    """Auth API test case."""

    def setUp(self):
        """Test case setup."""
        self.user = User.objects.create_user(
            first_name='Juan David',
            last_name='Arce Martinez',
            email="juandavid.arce@utp.edu.co",
            username='juandavid',
            password="prueba123",
            is_active = True,
        )

        # Auth
        self.token = Token.objects.create(user=self.user).key
        self.client.credentials(HTTP_AUTHORIZATION='Bearer {}'.format(self.token))

        # URL
        self.url = '/auth/'
        

    def test_response_success(self):
        """Verify request succeed."""
        data = {'password':'prueba123','user':'juandavid.arce@utp.edu.co'}
        request = self.client.post(self.url,data=data)
        self.assertEqual(request.status_code, status.HTTP_200_OK)

    def test_response_bad_request(self):
        """Verify request succeed."""
        data = {'user':'juandavid.arce@utp.edu.co'}
        request = self.client.post(self.url,data=data)
        self.assertEqual(request.status_code, status.HTTP_400_BAD_REQUEST)

    def test_response_invalid_credentials(self):
        """Verify request succeed."""
        data = {'password':'prueba12346','user':'juandavid.arce@utp.edu.co'}
        request = self.client.post(self.url,data=data)
        self.assertEqual(request.status_code, status.HTTP_401_UNAUTHORIZED)
        

    