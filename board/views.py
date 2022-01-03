from .models import board
from authentication.models import custom_user
from .serializer import boardserializer, ChatThreadSerializer, boardserializer1
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.decorators import action
# board의 목록, detail 보여주기, 수정하기, 삭제하기 모두 가능
class boardviewset(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    #permission 추가 두개다 통과해야함
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    #permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = board.objects.all()
    serializer_class = boardserializer
    print(serializer_class)
    # serializer.save() 재정의
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    #인스턴스를 할때마다 생성하나 보다
    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = boardserializer1
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        new_data = {}

        try:
            if request.user.nickname == instance.author.nickname:
                for i in serializer.data:
                    new_data[i] = serializer.data[i]
                new_data['is_author'] = True
                return Response(new_data)
        except:
            return Response(serializer.data)
        return Response(serializer.data)


@api_view(['POST',])
@permission_classes((permissions.IsAuthenticated, ))
def chat_start_view(request):
    if request.method == 'POST':
        for_thread = {}
        username1 = request.user
        obj = custom_user.objects.get(username=username1).nickname
        nickname2 = request.data.get('second_person')

        for_thread['first_person'] = obj
        for_thread['second_person'] = nickname2

        serializer = ChatThreadSerializer(data=for_thread)

        if serializer.is_valid():
            chat_thread = serializer.save()
            return JsonResponse({"message": "success"})
        else:
            data = serializer.errors
        return JsonResponse(data)
