# 아까 만든 RegistrationUserSerializer 임포트
from rest_framework.authtoken.models import Token
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import UserSerializer
from django.http import JsonResponse


@api_view(['POST', ])
@permission_classes((permissions.AllowAny,))
def registration_view(request):
    if request.method == 'POST':

        serializer = UserSerializer(data = request.data)
        data = {}

        if serializer.is_valid():

            account = serializer.save()

            data['response'] = "success"
            data['email'] = account.email
            data['username'] = account.username
            token = Token.objects.get(user=account).key
            data['token'] = token

        else:
            data = serializer.errors
        return JsonResponse(data)