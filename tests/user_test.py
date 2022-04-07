
from django.urls.base import reverse
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from django.test.testcases import TestCase


class SubscribeTest(APITestCase):
    def setUp(self):
        self.url = reverse('subscribe')
        
    def test_subscribe(self):
        resp = self.client.post(self.url, {'name': 'user',
                                           'email': 'user@foo.com',
                                           'password': 'pass'})

        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertTrue('result' in resp.data)
        self.assertTrue(resp.data['result'])


class UnsubscribeTest(APITestCase):
    def setUp(self):
        self.url = reverse('token_obtain_pair')
        self.url_unsubscribe = reverse('unsubscribe')
        
        user = User.objects.create_user(username = 'user_to_unsubscribe',
                                        email = 'user_to_unsubscribe@foo.com',
                                        password = 'pass')
        user.is_active = True
        user.save()

    def test_unsubscribe(self):
        resp = self.client.post(self.url, {'username': 'user_to_unsubscribe',
                                           'password': 'pass'}, format = 'json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

        self.assertTrue('access' in resp.data)
        self.assertTrue('refresh' in resp.data)
        
        access = resp.data['access']

        self.client.credentials(HTTP_AUTHORIZATION = 'Bearer ' + access)
        resp = self.client.post(self.url_unsubscribe, data = {'format': 'json'})
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertTrue('result' in resp.data)
        self.assertTrue(resp.data['result'])
        


class ChangePasswordTest(APITestCase):
    def setUp(self):
        self.url = reverse('token_obtain_pair')
        self.url_changepassword = reverse('changepassword')
        
        user = User.objects.create_user(username = 'user_to_change',
                                        email = 'user_to_change@foo.com',
                                        password = 'pass')
        user.is_active = True
        user.save()

    def test_changepassword(self):
        resp = self.client.post(self.url, {'username': 'user_to_change',
                                           'password': 'pass'}, format = 'json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

        self.assertTrue('access' in resp.data)
        self.assertTrue('refresh' in resp.data)
        
        access = resp.data['access']

        self.client.credentials(HTTP_AUTHORIZATION = 'Bearer ' + access)
        resp = self.client.post(self.url_changepassword, {'old_pass': 'pass',
                                                          'new_pass': 'newpass',
                                                          'confirm_pass': 'newpass'})
        
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertTrue('result' in resp.data)
        self.assertTrue(resp.data['result'])


