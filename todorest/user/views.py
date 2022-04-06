from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth.models import User
# Create your views here.

class NewView(APIView):
    # permission_classes = (IsAdminUser,)
    
    def post(self, request, format = None):
        user_name = request.POST.get("name")
        user_email = request.POST.get("email")
        user_password = request.POST.get("password")
        user_staff = request.POST.get("staff")
        
        if(user_name and user_email and user_password):
            search_user = User.objects.filter(username = user_name).first()
            
            result = False
            
            if(not search_user):
                user = User.objects.create_user(user_name, user_email, user_password)
                if(user_staff and user_staff.lower() == 'true'):
                    user.is_staff = True
                     
                user.save()
                result = True
                
            content = {'result': result}
                        
            return Response(content)


class DelView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def post(self, request, format = None):
        search_user = User.objects.filter(username = request.user).first()

        result = False
                
        if(search_user):
            search_user.delete()
            result = True
                
        content = {'result': result}
        
        return Response(content)


class PswView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def post(self, request, format = None):
        search_user = User.objects.filter(username = request.user).first()

        result = False
                
        if(search_user):
            old_pass = request.POST.get("old_pass")
            new_pass = request.POST.get("new_pass")
            confirm_pass = request.POST.get("confirm_pass")
            
            assert(len(new_pass) > 0)
            
            # if(old_pass and new_pass and confirm_pass and (new_pass == confirm_pass)):
            if(old_pass and new_pass and confirm_pass):
                search_user.user_password = new_pass
                search_user.save()
                result = True
                
        content = {'result': result}
        
        return Response(content)

    
    
    
    