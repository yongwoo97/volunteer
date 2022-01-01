from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from chat.models import Thread

@permission_classes((permissions.IsAuthenticated, ))
def messages_page(request):
    #여기서 프리패치를 쓰는 이유는 다대다인 채팅 데이터베이스의 쿼리값을 캐싱해서 보여주기 위함
    threads = Thread.objects.by_user(user=request.user).prefetch_related('chatmessage_thread').order_by('timestamp')
    context = {
        'Threads': threads
    }
    return render(request, 'messages.html', context)