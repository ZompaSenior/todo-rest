from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)
    
class AddUser(APIView):
    permission_classes = (IsAdminUser,)
    
    def post(self, request, format = None):
        content = {'data': request.data}
        return Response(content)        