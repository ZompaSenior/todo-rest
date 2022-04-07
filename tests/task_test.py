
from django.urls.base import reverse
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from datetime import datetime


class NewTaskTest(APITestCase):
    def setUp(self):
        self.url = reverse('token_obtain_pair')
        self.url_newtask = reverse('newtask')
        
        user = User.objects.create_user(username = 'user_for_task',
                                        email = 'user_for_task@foo.com',
                                        password = 'pass')
        user.is_active = True
        user.save()

    def test_newtask(self):
        resp = self.client.post(self.url, {'username': 'user_for_task',
                                           'password': 'pass'}, format = 'json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

        self.assertTrue('access' in resp.data)
        self.assertTrue('refresh' in resp.data)
        
        access = resp.data['access']

        self.client.credentials(HTTP_AUTHORIZATION = 'Bearer ' + access)
        resp = self.client.post(self.url_newtask, {'name': 'Prova',
                                                   'deadline': datetime.now(),
                                                   'description': 'Prova di task'})
        
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertTrue('result' in resp.data)
        self.assertTrue(resp.data['result'])


