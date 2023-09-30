from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.views import APIView
from .serializers import userserializer
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticated
import requests
# Create your views here.

class RegisterUser(APIView):
    def post(self,request):
        serializer = userserializer(data = request.data)
        if not serializer.is_valid():
            user = User.objects.get(username = serializer.data['username'])
            token_obj = Token.objects.get(user = user) 
            return Response({'status' : serializer.errors,'token' : str(token_obj)})
        serializer.save()
        user = User.objects.get(username = serializer.data['username'])
        token_obj = Token.objects.create(user = user)
        return Response({"status" : 200,'payload' : serializer.data,'token' : str(token_obj)})
    def get(self,request):
        auction = requests.get('http://127.0.0.1:8001/auction/')
        return Response({'auction':auction})
    
    


class adminAuthentication(BaseAuthentication):
    def authenticate(self, request):
        api_secret = request.META.get('HTTP_X_API_SECRET') 
        if api_secret == 'hsjwonxsnfsecretapiforadminoplmoqkilt':
            print(27)
            return (User.objects.first(),None)
        raise AuthenticationFailed('Forbidden')
    
class sample(APIView):
    authentication_classes = [adminAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request):
        user = User.objects.all()
        data = [{'name' : i.username} for i in user ]
        return Response({'users':data})    
    
    def post(self,request):
        serializer = userserializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(username = serializer.data['username'])
            token_obj = Token.objects.create(user = user)
            return Response({'message':'user created'})
        return Response({'message':'already exist'})

class AuctionAdmin(APIView):
    authentication_classes = [adminAuthentication]
    permission_classes = [IsAuthenticated]  
    def get(self,request):
        auction = requests.get('http://127.0.0.1:8001/auction/')
        return Response({'auction':auction})
    

