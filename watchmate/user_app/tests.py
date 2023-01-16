from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token


class RegisterTest(APITestCase):
    
    def test_register(self):
        data = {
            'username': 'testUser',
            'email': 'test@test.com',
            'password': 'test',
            'password_confirmation': 'test'
        }
        response = self.client.post(reverse('register'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    

class LoginLogoutTest(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='testUser', password= 'test123')
        
        
    def test_login(self):
        data = {
            'username': 'testUser',
            'password':'test123'
        }
        response = self.client.post(reverse('login'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_logout(self):
        self.token = Token.objects.get(user__username='testUser')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.post(reverse('logout'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

