"""Views to manage user subscription and profile."""

# Std Import
import shutil

# Site-package Import
from django.contrib.auth.models import User
from django.db.utils import IntegrityError

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from pathlib import PurePath

# Project Import
from todorest import settings
import os

class SubscribeView(APIView):
    """View to manage new user subscription."""
    
    def post(self, request, format = None):
        user_name = request.POST.get("name")
        user_email = request.POST.get("email")
        user_password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        
        result = False
        result_info = ''
        
        if(user_name and user_email and user_password):
            if(user_password == confirm_password):
                try:
                    user = User.objects.create_user(user_name, user_email, user_password)
                    user.is_staff = False
                         
                    user.save()
                    
                    result = True
                    
                except IntegrityError:
                    result_info = "User already present"
                    
                except Exception as e:
                    result_info = f"Error: {e}"
                    
            else:
                result_info = "Confirmation password does not match"
                
        else:
            result_info = "Not enough information"
                
        content = {'result': result,
                   'result_info': result_info}
                        
        return Response(content)


class UnsubscribeView(APIView):
    """View to manage user unsubscribe."""
    
    permission_classes = (IsAuthenticated,)
    
    def post(self, request, format = None):
        search_user = User.objects.filter(username = request.user).first()

        result = False
        result_info = ''
                
        if(search_user):
            user_id = search_user.id
            try:
                search_user.delete()
                
                user_folder = PurePath(settings.MEDIA_ROOT, f'user_{user_id}')
                
                try:
                    shutil.rmtree(user_folder)
                    
                    for root, dirs, files in os.walk(user_folder, topdown = False):
                        for name in dirs:
                            os.rmdir(os.path.join(root, name))
    
                    os.rmdir(user_folder)
                    
                except:
                    # TODO: A better management is required
                    pass
            
                result = True
    
            except Exception as e:
                result_info = f"Error: {e}"
            
        else:
            result_info = 'User not found'
                
        content = {'result': result,
                   'result_info': result_info}
        
        return Response(content)


class ChangePasswordView(APIView):
    """View to manage user password change."""
    
    permission_classes = (IsAuthenticated,)
    
    def post(self, request, format = None):
        search_user = User.objects.filter(username = request.user).first()

        result = False
        result_info = ''
                
        if(search_user):
            old_password = request.POST.get("old_password")
            new_password = request.POST.get("new_password")
            confirm_password = request.POST.get("confirm_password")
            
            if(old_password and new_password and confirm_password):
                if(new_password == confirm_password):
                    search_user.user_password = new_password
                    try:
                        search_user.save()
                        result = True
                        
                    except Exception as e:
                        result_info = f"Error: {e}"
                    
                else:
                    result_info = "Confirmation password does not match"
                
            else:
                result_info = "Not enough information"
                
        content = {'result': result,
                   'result_info': result_info}
        
        return Response(content)

    
    
    
    