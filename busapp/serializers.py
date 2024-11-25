from rest_framework import serializers

from .models import Appuser, Businfo

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appuser
        fields = ['id','name','phone']

class BusInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Businfo
        fields = '__all__'
