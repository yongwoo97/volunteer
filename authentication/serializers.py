from .models import custom_user
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model = custom_user
        fields = ('username', 'password', 'nickname')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        user = custom_user(
            username=self.validated_data['username'],
            password=self.validated_data['password'],
            nickname=self.validated_data['nickname']
        )
        user.set_password(self.validated_data['password'])
        user.save()
        return user


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = custom_user
        fields = ('username', 'nickname')

class YourProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = custom_user
        fields = ('nickname')