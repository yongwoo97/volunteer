from .models import board
from rest_framework import serializers
from chat.models import Thread

class boardserializer(serializers.ModelSerializer):
    class Meta:
        model = board
        fields = '__all__'

class boardserializer1(serializers.ModelSerializer):
    is_author = serializers.BooleanField(default=False)
    class Meta:
        model = board
        fields = '__all__'

class ChatThreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thread
        fields = '__all__'