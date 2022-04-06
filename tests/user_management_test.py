
from django.urls.base import reverse
from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status


class SubscribeTest(TestCase):
    def setUp(self):
        self.url = reverse('new')
        
    def test_new_user(self):
        resp = self.client.post(self.url, {'name': 'user',
                                           'email': 'user@foo.com',
                                           'password': 'pass'}, format = 'json')

        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertTrue('result' in resp.data)
        self.assertTrue(resp.data['result'])


class ChangePasswordTest(APITestCase):
    def setUp(self):
        self.url = reverse('token_obtain_pair')
        self.url_psw = reverse('psw')
        
        user = User.objects.create_user(username = 'user_to_change',
                                        email = 'user_to_change@foo.com',
                                        password = 'pass')
        user.is_active = True
        user.save()

    def test_api_jwt(self):
    
        resp = self.client.post(self.url, {'username': 'user_to_change',
                                           'password': 'pass'}, format = 'json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

        self.assertTrue('access' in resp.data)
        self.assertTrue('refresh' in resp.data)
        
        access = resp.data['access']

        self.client.credentials(HTTP_AUTHORIZATION = 'Bearer ' + access)
        resp = self.client.post(self.url_psw, {'old_pass': 'pass',
                                               'new_pass': 'newpass',
                                               'confirm_pass': 'newpass'}, format = 'json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertTrue('result' in resp.data)
        self.assertTrue(resp.data['result'])


class UnsubscribeTest(APITestCase):
    def setUp(self):
        self.url = reverse('token_obtain_pair')
        self.url_del = reverse('del')
        
        user = User.objects.create_user(username = 'user_to_unsubscribe',
                                        email = 'user_to_unsubscribe@foo.com',
                                        password = 'pass')
        user.is_active = True
        user.save()

    def test_api_jwt(self):
    
        resp = self.client.post(self.url, {'username': 'user_to_unsubscribe',
                                           'password': 'pass'}, format = 'json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

        self.assertTrue('access' in resp.data)
        self.assertTrue('refresh' in resp.data)
        
        access = resp.data['access']

        self.client.credentials(HTTP_AUTHORIZATION = 'Bearer ' + access)
        resp = self.client.post(self.url_del, data = {'format': 'json'})
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertTrue('result' in resp.data)
        self.assertTrue(resp.data['result'])
        
