
from django.urls.base import reverse
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from datetime import datetime

test_file_1 = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADMAAAAzCAIAAAC1w6d9AAAAh3pUWHRSYXcgcHJvZmlsZSB0eXBlIGV4aWYAAHjadY7LDcQwCETvVJESMOAByllFiZQOtvzFcqzksu8AoxGfoeN7nbQNGgtZ90ACXFhayqdE8ESZm3Abverk7tpKyWOTyhTIcLZn0G5/0RWB080dHTt2qetyqGhUrT0aV3nEyNc3XYn++CvFD0K+LCGFVYifAAAKAmlUWHRYTUw6Y29tLmFkb2JlLnhtcAAAAAAAPD94cGFja2V0IGJlZ2luPSLvu78iIGlkPSJXNU0wTXBDZWhpSHpyZVN6TlRjemtjOWQiPz4KPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczptZXRhLyIgeDp4bXB0az0iWE1QIENvcmUgNC40LjAtRXhpdjIiPgogPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4KICA8cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0iIgogICAgeG1sbnM6ZXhpZj0iaHR0cDovL25zLmFkb2JlLmNvbS9leGlmLzEuMC8iCiAgICB4bWxuczp0aWZmPSJodHRwOi8vbnMuYWRvYmUuY29tL3RpZmYvMS4wLyIKICAgZXhpZjpQaXhlbFhEaW1lbnNpb249IjUxIgogICBleGlmOlBpeGVsWURpbWVuc2lvbj0iNTEiCiAgIHRpZmY6SW1hZ2VXaWR0aD0iNTEiCiAgIHRpZmY6SW1hZ2VIZWlnaHQ9IjUxIgogICB0aWZmOk9yaWVudGF0aW9uPSIxIi8+CiA8L3JkZjpSREY+CjwveDp4bXBtZXRhPgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgCjw/eHBhY2tldCBlbmQ9InciPz5pZgYrAAAAA3NCSVQICAjb4U/gAAAAR0lEQVRYw+3OsREAEBAAQfT+ORHdviJeINgr4GZ7ZranxVmxZ/0z2q+RkZGRkZGRkZGRkZGRkZGRkZGRkZGRkZGRkZGRkVW7puAGvSEr+egAAAAASUVORK5CYII="

test_file_2 = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAIAAACRXR/mAAAAh3pUWHRSYXcgcHJvZmlsZSB0eXBlIGV4aWYAAHjadY7BDcQwCAT/VJESMOAFyjlFiZQOrvzDcqzkc/OA1QoW6PheJ22DxkLWPZAAF5aW8ikRPFHmJtxGrzq5u7ZS8tikMgUynO0ZtNtfdEXgdHNHx45dKl0OFY2qtUcjlccb+bq2QvSPv774AUKGLB/gq36pAAAKAmlUWHRYTUw6Y29tLmFkb2JlLnhtcAAAAAAAPD94cGFja2V0IGJlZ2luPSLvu78iIGlkPSJXNU0wTXBDZWhpSHpyZVN6TlRjemtjOWQiPz4KPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczptZXRhLyIgeDp4bXB0az0iWE1QIENvcmUgNC40LjAtRXhpdjIiPgogPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4KICA8cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0iIgogICAgeG1sbnM6ZXhpZj0iaHR0cDovL25zLmFkb2JlLmNvbS9leGlmLzEuMC8iCiAgICB4bWxuczp0aWZmPSJodHRwOi8vbnMuYWRvYmUuY29tL3RpZmYvMS4wLyIKICAgZXhpZjpQaXhlbFhEaW1lbnNpb249IjUwIgogICBleGlmOlBpeGVsWURpbWVuc2lvbj0iNTAiCiAgIHRpZmY6SW1hZ2VXaWR0aD0iNTAiCiAgIHRpZmY6SW1hZ2VIZWlnaHQ9IjUwIgogICB0aWZmOk9yaWVudGF0aW9uPSIxIi8+CiA8L3JkZjpSREY+CjwveDp4bXBtZXRhPgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgCjw/eHBhY2tldCBlbmQ9InciPz6tm16TAAAAA3NCSVQICAjb4U/gAAABAUlEQVRYw+3ZOxKCMBAG4MSx8RaewArHNNB6BWsrU0GfOr1Uch4oxIE7YbGKFRIgD4r/rxhmgG92eSwT3nUdW182bJUBCyywwALLSrbWz6iLvN+umrps69FDkkjER8EYU7eU9vAl38Sqrcv2ZX55kySRUDKdzKJi6Mc9fBP9UIxY1CCL3VnEIo3PwoywdJEH1/xYushDdepP+O6wx1seLLDAAgsssFzM8lNHZJriKf0s74+lZPalnOJIhKlWj+gLEKaJ1A6TSjhnUUnm1cMyyx1lDkvJzFaDLLA8a0ZY9MftXzPIUjJzfd9MYNHjvQbQJ+frpWye3crCsbgCFlhgDeUNRU3xJbLa0C4AAAAASUVORK5CYII="


PAGE_SIZE = 25

class TaskTest(APITestCase):
    
    def setUp(self):
        self.url = reverse('token_obtain_pair')
        self.url_newtask = reverse('newtask')
        self.url_edittask = reverse('edittask')
        self.url_deletetask = reverse('deletetask')
        self.url_tasklist = reverse('tasklist')
        self.url_unsubscribe = reverse('unsubscribe')
        
        user = User.objects.create_user(username = 'user_for_task',
                                        email = 'user_for_task@foo.com',
                                        password = 'pass')
        user.is_active = True
        user.save()
        
        self.pk = 0

    def subtest_newtask(self):
        resp = self.client.post(self.url, {'username': 'user_for_task',
                                           'password': 'pass'}, format = 'json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

        self.assertTrue('access' in resp.data)
        self.assertTrue('refresh' in resp.data)
        
        access = resp.data['access']

        self.client.credentials(HTTP_AUTHORIZATION = 'Bearer ' + access)
        resp = self.client.post(self.url_newtask, {'name': 'Prova',
                                                   'deadline': datetime.now(),
                                                   'description': 'Prova di task',
                                                   'image': test_file_1})
        
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertTrue('result' in resp.data)
        self.assertTrue(resp.data['result'])
        self.assertEqual(resp.data['pk'], 1)
        
        self.pk = resp.data['pk']

    def subtest_edittask(self):
        resp = self.client.post(self.url, {'username': 'user_for_task',
                                           'password': 'pass'}, format = 'json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

        self.assertTrue('access' in resp.data)
        self.assertTrue('refresh' in resp.data)
        
        access = resp.data['access']

        self.client.credentials(HTTP_AUTHORIZATION = 'Bearer ' + access)
        resp = self.client.post(self.url_edittask, {'pk': self.pk,
                                                    'name': 'Prova2',
                                                   'deadline': datetime.now(),
                                                   'description': 'Prova di task 2',
                                                   'image': test_file_2})
        
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertTrue('result' in resp.data)
        self.assertTrue(resp.data['result'])

    def subtest_deletetask(self):
        resp = self.client.post(self.url, {'username': 'user_for_task',
                                           'password': 'pass'}, format = 'json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

        self.assertTrue('access' in resp.data)
        self.assertTrue('refresh' in resp.data)
        
        access = resp.data['access']

        self.client.credentials(HTTP_AUTHORIZATION = 'Bearer ' + access)
        resp = self.client.post(self.url_deletetask, {'pk': self.pk})
        
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertTrue('result' in resp.data)
        self.assertTrue(resp.data['result'])

    def test_complete_edit(self):
        self.subtest_newtask()
        self.subtest_edittask()
        self.subtest_deletetask()
        
    def test_listtask(self):
        resp = self.client.post(self.url, {'username': 'user_for_task',
                                           'password': 'pass'}, format = 'json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

        self.assertTrue('access' in resp.data)
        self.assertTrue('refresh' in resp.data)
        
        access = resp.data['access']

        pk_list = []
        for i in range(1000):
            self.client.credentials(HTTP_AUTHORIZATION = 'Bearer ' + access)
            resp = self.client.post(self.url_newtask, {'name': f'Test_{i}',
                                                       'deadline': datetime.now(),
                                                       'description': f'Task test {i}',
                                                       'image': test_file_1})

            self.assertEqual(resp.status_code, status.HTTP_200_OK)
            self.assertTrue('result' in resp.data)
            self.assertTrue(resp.data['result'])
            pk_list.append(resp.data['pk'])
        
        request_parameters = {'order_field': 'name',
                              'page_size': PAGE_SIZE,
                              'page_number': 0,
                              'image_format': 'url'}
        
        for p in range(1, int(1000 / PAGE_SIZE), 1):
            self.client.credentials(HTTP_AUTHORIZATION = 'Bearer ' + access)
            request_parameters['page_number'] = p
            resp = self.client.post(self.url_tasklist, request_parameters)
            
            self.assertEqual(resp.status_code, status.HTTP_200_OK)
            self.assertTrue('result' in resp.data)
            self.assertTrue(resp.data['result'])
            self.assertTrue('task_page' in resp.data)
            
        request_parameters['order_field'] = 'deadline'
        
        for p in range(1, int(1000 / PAGE_SIZE), 1):
            self.client.credentials(HTTP_AUTHORIZATION = 'Bearer ' + access)
            request_parameters['page_number'] = p
            resp = self.client.post(self.url_tasklist, request_parameters)
            
            self.assertEqual(resp.status_code, status.HTTP_200_OK)
            self.assertTrue('result' in resp.data)
            self.assertTrue(resp.data['result'])
            self.assertTrue('task_page' in resp.data)
        
        for pk in pk_list:
            self.client.credentials(HTTP_AUTHORIZATION = 'Bearer ' + access)
            resp = self.client.post(self.url_deletetask, {'pk': pk})
        
            self.assertEqual(resp.status_code, status.HTTP_200_OK)
            self.assertTrue('result' in resp.data)
            self.assertTrue(resp.data['result'])
        
    def tearDown(self):
        resp = self.client.post(self.url, {'username': 'user_for_task',
                                           'password': 'pass'}, format = 'json')
        access = resp.data['access']
        
        self.client.credentials(HTTP_AUTHORIZATION = 'Bearer ' + access)
        resp = self.client.post(self.url_unsubscribe, data = {'format': 'json'})
        
        
        
        