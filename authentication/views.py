# 아까 만든 RegistrationUserSerializer 임포트
from rest_framework.authtoken.models import Token
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from .serializers import UserSerializer
from django.http import JsonResponse
from django.contrib.auth import authenticate

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


#로그인 뷰, 아이디 패스워드 체크하고 맞으면 토큰 발급
@api_view(['POST'])
@permission_classes((permissions.AllowAny, ))
def login_view(request):
    if request.method == 'POST':
        email = request.data.get('email')
        print(email)
        password = request.data.get('password')

        user = authenticate(username = email, password = password)
        if not user:
            return JsonResponse({'error': 'invalid user'})

        token, _ = Token.objects.get_or_create(user=user)
        return JsonResponse({'token': token.key})
#프로필 get view 자기 프로필이면 반환
