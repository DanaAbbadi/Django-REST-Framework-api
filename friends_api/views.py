from django.shortcuts import render
from rest_framework import generics

from .models import Friends
from .serializer import FriendsSerializer
# Create your views here.

class FriendsList(generics.ListCreateAPIView):
    queryset = Friends.objects.all()
    serializer_class = FriendsSerializer

class FriendsDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Friends.objects.all()
    serializer_class = FriendsSerializer


