from .models import board
from rest_framework import serializers

class boardserializer(serializers.ModelSerializer):
    class Meta:
        model = board
        fields = '__all__'