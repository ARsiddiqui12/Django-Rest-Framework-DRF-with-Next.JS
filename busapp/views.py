from django.shortcuts import render

from  rest_framework import  generics

from .models import Appuser

from  .serializers import PostSerializer

class AppuserListView(generics.ListCreateAPIView):
    queryset = Appuser.objects.all()
    serializer_class = PostSerializer

class AppuserDetailView(generics.RetrieveUpdateAPIView):
    queryset = Appuser.objects.all()
    serializer_class = PostSerializer

# Create your views here.
