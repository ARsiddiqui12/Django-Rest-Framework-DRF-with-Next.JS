from rest_framework import serializers

from .models import Appuser

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appuser
        fields = ['name','phone']