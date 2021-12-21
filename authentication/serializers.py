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
            email=self.validated_data['email'],
            username=self.validated_data['username'],
            purpose=self.validated_data['purpose'],
            password = self.validated_data['password'],
            belong=self.validated_data['belong']
        )
        user.save()
        return user