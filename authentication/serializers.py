from .models import custom_user
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model = custom_user
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }


    def save(self):
        user = custom_user(
            username=self.validated_data['username'],
            nickname=self.validated_data['nickname'],
            purpose=self.validated_data['purpose'],
            belong=self.validated_data['belong']
        )
        user.set_password(self.validated_data['password'])
        user.save()
        return user