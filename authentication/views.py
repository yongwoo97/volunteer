# 아까 만든 RegistrationUserSerializer 임포트
from rest_framework.authtoken.models import Token
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from .serializers import UserSerializer, ProfileSerializer
from django.contrib.auth import authenticate

#여기는 메일 인증을 위해 사용한 것들
from .models import custom_user
import jwt
from .text import message
from authentication.my_settings import SECRET_KEY
from django.views import View
from django.http import JsonResponse
from django.core.exceptions import ValidationError
from django.shortcuts import redirect
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from .tasks import sending_email
from .permissions import IsOwnerOrNothing

@api_view(['GET', ])
@permission_classes((IsOwnerOrNothing, ))
def request_profile(request):
    if request.method == 'GET':
        try:
            userobj = request.user
            qs = custom_user.objects.get(username=userobj.username)
            serializer = ProfileSerializer(qs)

            return JsonResponse(serializer.data)
        except:
            return JsonResponse({"error": "invalid user"})


@api_view(['POST', ])
@permission_classes((permissions.AllowAny,))
def registration_view(request):
    if request.method == 'POST':

        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():

            user = serializer.save()

            current_site = get_current_site(request)
            domain = current_site.domain
            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
            token = jwt.encode({'user':user.id}, SECRET_KEY['secret'], algorithm=SECRET_KEY['algorithm'])
            message_data = message(domain, uidb64, token)

            #이메일을 보내는 프로세스가 약 5초 정도 걸리는데 이러면 너무 오래걸려서 비동기적으로 처리할 예정
            sending_email.delay(message_data, user.username)
            return JsonResponse({'message':'success'}, status = 200)
        else:
            data = serializer.errors
        return JsonResponse(data)


#로그인 뷰, 아이디 패스워드 체크하고 맞으면 토큰 발급
@api_view(['POST'])
@permission_classes((permissions.AllowAny, ))
def login_view(request):
    if request.method == 'POST':
        username = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if not user:
            return JsonResponse({'message': 'invalid user'})

        token, _ = Token.objects.get_or_create(user=user)
        return JsonResponse({'token': token.key}, status = 200)

#닉네임 중복 확인
@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def nickname_check(request):
    if request.method == 'POST':
        nickname = request.data.get('nickname')
        try:
            db_nickname = custom_user.objects.get(nickname=nickname)
            return JsonResponse({'message': 'already exists'})
        except:
            return JsonResponse({'message' : 'possible nickname'})


class Activate(View):
    def get(self, request, uidb64, token):
        try:
            #클라이언트에서 요청온 uidb64를 디코딩
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = custom_user.objects.get(pk=uid)

            #토큰을 디코딩해서 비교할 pk값 생성
            user_dic = jwt.decode(token, SECRET_KEY['secret'], algorithms=SECRET_KEY['algorithm'])

            if user.id == user_dic['user']:
                user.is_active = True
                user.save()
                #리다이렉트를 어디로 설정할 것인가? 메인페이지로 호출해야겠지
                return redirect('http://15.164.62.156:8888/api/board/')

            return JsonResponse({'message' : 'auth_fail'}, status=400)
        except ValidationError:
            return JsonResponse({'message' : 'type_error'}, status=400)
        except KeyError:
            return JsonResponse({'message' : 'invalid_key'}, status=400)

