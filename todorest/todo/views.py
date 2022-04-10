"""Views to manage user subscription and profile."""

# Std Import
import base64
import os
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
from django.forms.models import model_to_dict

IMAGE_FORMAT_DATA = 'data'
IMAGE_FORMAT_URL = 'url'


def base64_file(data):
    """Commodity function to decode uploaded image."""
    
    _format, _img_str = data.split(';base64,')
    _name, ext = _format.split('/')
        
    return ContentFile(base64.b64decode(_img_str), name='{}.{}'.format(uuid.uuid4(), ext))


def task_to_dict(task, image_format):
    """Convert the task into a dictionary"""
    
    task_dict = model_to_dict(task, exclude = ['image'])
    
    if(image_format == IMAGE_FORMAT_DATA):
        task_dict['image'] = base64.b64encode(task.image.file.read())
        
    elif(image_format == IMAGE_FORMAT_URL):
        task_dict['image'] = task.image.url
        
    else:
        task_dict['image'] = "Error: format not supported"
    
    return task_dict


class NewTaskView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def post(self, request, format = None):
        """Creation of a new Task.
        
        Args:
            name: name of the Task
            description: a brief description
            deadline: deadline of the Task
            image: an image to associate to the Task in base64 format
            
        Returns:
            result: True if ok
            result_info: a description of the error if present
            pk: the identiti of the new created Task
        """
        user = User.objects.filter(username = request.user).first()

        result = False
        result_info = ''
        
        name = request.POST.get("name")
        
        if(user):
            with transaction.atomic():
                if(not user.tasks.filter(name = name).first()):
                    task = models.Task()
                    task.name = name
                    task.deadline = request.POST.get("deadline")
                    task.description = request.POST.get("description")
                    task.image = base64_file(request.POST.get("image"))
                    task.user = user
                    task.save()
                    
                    result = True
                    
                else:
                    result_info = 'Duplicated Task'
                
        else:
            result_info = 'User not found'
                
        content = {'result': result,
                   'result_info': result_info,
                   'pk': task.pk if task else 0}
        
        return Response(content)
    
    
class EditTaskView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def post(self, request, format = None):
        """Edit a present Task.
        
        It is possible to edit only Task of the logged user.
        
        Args:
            pk: identity of the Task to edit
            name: name of the Task
            description: a brief description
            deadline: deadline of the Task
            image: an image to associate to the Task in base64 format
            
        Returns:
            result: True if ok
            result_info: a description of the error if present
        """

        user = User.objects.filter(username = request.user).first()

        result = False
        result_info = ''
        
        pk = request.POST.get("pk")
        
        if(user):
            with transaction.atomic():
                task = user.tasks.filter(pk = pk).first()
                
                if(task):
                    task.name = request.POST.get("name")
                    task.description = request.POST.get("description")
                    task.deadline = request.POST.get("deadline")
                    old_image_path = task.image.path
                    task.image = base64_file(request.POST.get("image"))
                    task.user = user
                    task.save()
                    
                    os.remove(old_image_path)
                    
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
        """Delete a present Task.
        
        It is possible to delete only Task of the logged user.
        
        Args:
            pk: identity of the Task to delete
            
        Returns:
            result: True if ok
            result_info: a description of the error if present
        """
        
        user = User.objects.filter(username = request.user).first()

        result = False
        result_info = ''
        
        pk = request.POST.get("pk")
        
        if(user):
            with transaction.atomic():
                task = user.tasks.filter(pk = pk).first()
                
                if(task):
                    old_image_path = task.image.path
                    task.delete()
                    os.remove(old_image_path)
                    
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
        """List user Tasks.
        
        Args:
            order_field: field to order by the list.
                Possible value are:
                > name: ordered by name
                > deadline: ordered by deadline
            page_size: the size of the pages for the paginator
            page_number: current page to retrieve
            image_format: the format to retrieve the image.
                Possible value are:
                > data: return in the list entire image 
                > url: return only a url, for async download them
            
        Returns:
            result: True if ok
            result_info: a description of the error if present
            task_page: current requested page list of Task
        """
        
        user = User.objects.filter(username = request.user).first()

        result = False
        result_info = ''
        
        # TODO: manage some default value
        order_field = request.POST.get("order_field")
        page_size = request.POST.get("page_size")
        page_number = request.POST.get("page_number")
        image_format = request.POST.get("image_format")
        
        if(user):
            if(order_field in ('name', 'deadline')):
                # TODO: manage the direction of the order by (ASC o DESC)
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
                   'task_page': [task_to_dict(task, image_format) for task in task_page]}
        
        return Response(content)
    