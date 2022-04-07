
from django.urls.base import reverse
from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status


class WrongLoginTest(TestCase):
    def setUp(self):
        self.url = reverse('token_obtain_pair')
        
    def test_wrong_login(self):
        resp = self.client.post(self.url, {'username': 'user_not_present',
                                           'password': 'pass'}, format = 'json')
        self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)


class NotAuthorizedLoginTest(TestCase):
    def setUp(self):
        self.url = reverse('token_obtain_pair')
        
        user = User.objects.create_user(username = 'user_not_active',
                                        email = 'user_not_active@foo.com',
                                        password = 'pass')
        user.is_active = False
        user.save()
        
    def test_not_authorized_login(self):
        resp = self.client.post(self.url, {'username': 'user_not_active',
                                           'password': 'pass'}, format = 'json')
        self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)


class LoginTest(TestCase):
    def setUp(self):
        self.url = reverse('token_obtain_pair')
        
        user = User.objects.create_user(username = 'user_active',
                                        email = 'user@foo.com',
                                        password = 'pass')
        user.is_active = True
        user.save()

    def test_login(self):
    
        resp = self.client.post(self.url, {'username': 'user_active',
                                           'password': 'pass'}, format = 'json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

        self.assertTrue('access' in resp.data)
        self.assertTrue('refresh' in resp.data)
