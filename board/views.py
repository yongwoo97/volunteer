from .models import board
from authentication.models import custom_user
from .serializer import boardserializer, ChatThreadSerializer, boardserializer1
from rest_framework import viewsets, status
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

    #오버라이드하는걸 어떻게 하면 간편하게 할 수 있을까?
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset()).reverse()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        #오버라이드된 부분
        request.data['author'] = self.request.user.nickname

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        # 오버라이드된 부분
        request.data['author'] = self.request.user.nickname

        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)


    #인스턴스를 할때마다 생성하나 보다
    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = boardserializer1
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        instance.counter += 1
        instance.save()

        new_data = {}
        for i in serializer.data:
            new_data[i] = serializer.data[i]

        try:
            if request.user.nickname == instance.author.nickname:
                new_data['is_author'] = True
        except:
            pass

        return Response(new_data)

    @action(detail=False, methods=['GET'], url_path='my_list')
    def my_list(self, request):
        qs = self.queryset.filter(author=request.user.nickname).reverse()
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['POST'], url_path='your_list')
    def your_list(self, request):
        qs = self.queryset.filter(author=request.data.get('author')).reverse()
        serializer = self.get_serializer(qs, many=True)
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
