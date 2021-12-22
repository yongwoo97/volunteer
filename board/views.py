from .models import board
from .serializer import boardserializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly
from rest_framework.decorators import action
# board의 목록, detail 보여주기, 수정하기, 삭제하기 모두 가능
class boardviewset(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    #permission 추가
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    queryset = board.objects.all()
    serializer_class = boardserializer

    # serializer.save() 재정의
    @action(methods=['POST'], detail=True)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)