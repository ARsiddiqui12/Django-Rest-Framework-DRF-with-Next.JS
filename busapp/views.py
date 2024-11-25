from symtable import Class

from django.shortcuts import render

from rest_framework import generics, status
from rest_framework.response import Response

from .models import Appuser, Businfo

from  .serializers import PostSerializer,BusInfoSerializer

class AppuserListView(generics.ListCreateAPIView):
    queryset = Appuser.objects.all()
    serializer_class = PostSerializer

class AppuserDetailView(generics.RetrieveUpdateAPIView):
    queryset = Appuser.objects.all()
    serializer_class = PostSerializer

    def delete(self, request, *args, **kwargs):
        try:
            # Get the object based on the primary key
            instance = self.get_object()
            instance.delete()  # Perform the delete operation
            return Response({"message": "Deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class BusinfoListView(generics.ListCreateAPIView):
    queryset = Businfo.objects.all()
    serializer_class = BusInfoSerializer

class BusinfoDetailView(generics.RetrieveUpdateAPIView):
    queryset = Appuser.objects.all()
    serializer_class = PostSerializer

    def delete(self, request, *args, **kwargs):
        try:
            # Get the object based on the primary key
            instance = self.get_object()
            instance.delete()  # Perform the delete operation
            return Response({"message": "Deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


