from django.shortcuts import render
from rest_framework import generics,viewsets
from .models import User
from .serializers import UserSerializer

# Create your views here.

class UsersList(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer