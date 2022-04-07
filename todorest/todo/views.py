"""Views to manage user subscription and profile."""

# Std Import
import base64
import uuid

# Site-package Import
from django.contrib.auth.models import User
from django.core.files.base import ContentFile
from django.db import transaction

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Project Import
from . import models
from django.core.paginator import Paginator

def base64_file(data):
    """Commodity function to decode uploaded image."""
    
    _format, _img_str = data.split(';base64,')
    _name, ext = _format.split('/')
        
    return ContentFile(base64.b64decode(_img_str), name='{}.{}'.format(uuid.uuid4(), ext))

class NewTaskView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def post(self, request, format = None):
        user = User.objects.filter(username = request.user).first()

        result = False
        result_info = ''
        
        name = request.POST.get("name")
        
        if(user):
            with transaction.atomic():
                if(not user.tasks.filter(name = name).first()):
                    task = models.Task()
                    task.name = name
                    task.image = base64_file(request.POST.get("image"))
                    task.deadline = request.POST.get("deadline")
                    task.description = request.POST.get("description")
                    task.user = user
                    task.save()
                    
                    result = True
                    
                else:
                    result_info = 'Duplicated Task'
                
        else:
            result_info = 'User not found'
                
        content = {'result': result,
                   'result_info': result_info}
        
        return Response(content)
    
    
class EditTaskView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def post(self, request, format = None):
        user = User.objects.filter(username = request.user).first()

        result = False
        result_info = ''
        
        name = request.POST.get("name")
        
        if(user):
            with transaction.atomic():
                task = user.tasks.filter(name = name).first()
                
                if(task):
                    task.name = name
                    task.image = base64_file(request.POST.get("image"))
                    task.deadline = request.POST.get("deadline")
                    task.description = request.POST.get("description")
                    task.user = user
                    task.save()
                    
                    result = True
                    
                else:
                    result_info = 'Task not found'
                
        else:
            result_info = 'User not found'
                
        content = {'result': result,
                   'result_info': result_info}
        
        return Response(content)


class DeleteTaskView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def post(self, request, format = None):
        user = User.objects.filter(username = request.user).first()

        result = False
        result_info = ''
        
        name = request.POST.get("name")
        
        if(user):
            with transaction.atomic():
                task = user.tasks.filter(name = name).first()
                
                if(task):
                    # TODO: Clear file content
                    task.delete()
                    
                    result = True
                    
                else:
                    result_info = 'Task not found'
                
        else:
            result_info = 'User not found'
                
        content = {'result': result,
                   'result_info': result_info}
        
        return Response(content)    
    
    
class TaskListView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def post(self, request, format = None):
        user = User.objects.filter(username = request.user).first()

        result = False
        result_info = ''
        
        order_field = request.POST.get("order_field")
        page_size = request.POST.get("page_size")
        page_number = request.POST.get("page_number")
        
        if(user):
            if(order_field in ('name', 'deadline')):
                tasks = user.tasks.order_by(order_field)
                paginator = Paginator(tasks, page_size)
                task_page = paginator.get_page(page_number)
                result = True
                
            else:
                result_info = 'order_field not admitted'
                
        else:
            result_info = 'User not found'
                
        content = {'result': result,
                   'result_info': result_info,
                   'task_page': task_page}
        
        return Response(content)
    