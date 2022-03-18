"""user tests."""

# Django REST Framework
from rest_framework import status
from rest_framework.test import APITestCase

# Model
from users.models import User
from rest_framework.authtoken.models import Token




class UserAPITestCase(APITestCase):
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
        self.url = '/user/'
        

    def test_response_success(self):
        """Verify request succeed."""
        request = self.client.get(self.url)
        self.assertEqual(request.status_code, status.HTTP_200_OK)
    
    def test_response_invalid_token(self):
        """Verify if the client send an invalid token."""
        self.client.credentials(HTTP_AUTHORIZATION='Bearer {}'.format(self.token+"d"))
        request = self.client.get(self.url)
        self.assertEqual(request.status_code, status.HTTP_401_UNAUTHORIZED)

    
        

    