
# 아까 만든 RegistrationUserSerializer 임포트
from rest_framework.authtoken.models import Token
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import RegistrationUserSerializer
from django.contrib.auth.models import update_last_login
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth import get_user_model


# POST 로 데이터를 받을 것임을 명시해준다.
@api_view(['POST', ])
# 토큰이 없으면 페이지를 못들어온다. 때문에, 이 페이지에 관해서
# 권한을 다르게 설정해준다.
@permission_classes((permissions.AllowAny,))
def registration_view(request):
    # 요청의 메써드가 POST이면,
    if request.method == 'POST':

        # serializer를 불러와 request.data 를 집어넣는다.
        serializer = RegistrationUserSerializer(data=request.data)

        # 응답으로 보내줄 data의 초기화
        data = {}

        # serializer가 data 맛을 보고 이게 옳다 싶으면
        # .is_valid()를 True로 뱉는다.
        if serializer.is_valid():

            # serializer.save()를 거치면 저장을 한다.
            account = serializer.save()

            # 그치만, 저장이 됐는지를 응답을 해줘야 하므로 아래와 같이 응답데이터를 구성해준다.
            data['response'] = "successfully registred a new user"
            data['email'] = account.email
            data['username'] = account.username
            token = Token.objects.get(user=account).key
            print(token)
            data['token'] = token

        else:
            data = serializer.errors
        print('done!!!!!!!!!!')
        return Response(data)


@api_view(['GET', ])
# @permission_classes((permissions.IsAuthenticated, ))
def example_view(request, format=None):
    content = {
        'user': str(request.user),
        'userRole': request.user.RoleUser.userType,
        'result': 'Authenticated'
    }
    return Response(content)


# 토큰 취득시, last_login을 업데이트 해준다.
class TokenAuthenticationView(ObtainAuthToken):
    """Implementation of ObtainAuthToken with last_login update"""

    def post(self, request):
        result = super(TokenAuthenticationView, self).post(request)
        currentUserModel = get_user_model()
        try:
            user = currentUserModel.objects.get(username=request.data['username'])
            update_last_login(None, user)
        except Exception as exc:
            return None
        return result