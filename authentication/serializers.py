from .models import custom_user
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model = custom_user
        fields = '__all__'
        extra_kwargs = {
            'password1': {'write_only': True},
            'password2': {'write_only': True}
        }


    def save(self):
        user = custom_user(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
            purpose=self.validated_data['purpose'],
            belong=self.validated_data['belong']
        )

        password1 = self.validated_data['password1']
        password2 = self.validated_data['password2']
        if password1 != password2:
            raise serializers.ValidationError('check')

        user.save()
        return user