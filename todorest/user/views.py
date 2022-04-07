"""Views to manage user subscription and profile."""

# Std Import

# Site-package Import
from django.contrib.auth.models import User
from django.db.utils import IntegrityError

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Project Import

class SubscribeView(APIView):
    """View to manage new user subscription."""
    
    def post(self, request, format = None):
        user_name = request.POST.get("name")
        user_email = request.POST.get("email")
        user_password = request.POST.get("password")
        user_staff = request.POST.get("staff")
        
        result = False
        result_info = ''
        
        if(user_name and user_email and user_password):
            
            try:
                user = User.objects.create_user(user_name, user_email, user_password)
                if(user_staff and user_staff.lower() == 'true'):
                    user.is_staff = True
                     
                user.save()
                result = True
                
            except IntegrityError:
                result_info = "User already present"
                
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
                
        if(search_user):
            search_user.delete()
            result = True
                
        content = {'result': result}
        
        return Response(content)


class ChangePasswordView(APIView):
    """View to manage user password change."""
    
    permission_classes = (IsAuthenticated,)
    
    def post(self, request, format = None):
        search_user = User.objects.filter(username = request.user).first()

        result = False
                
        if(search_user):
            old_pass = request.POST.get("old_pass")
            new_pass = request.POST.get("new_pass")
            confirm_pass = request.POST.get("confirm_pass")
            
            if(old_pass and new_pass and confirm_pass and (new_pass == confirm_pass)):
                search_user.user_password = new_pass
                search_user.save()
                result = True
                
        content = {'result': result}
        
        return Response(content)

    
    
    
    