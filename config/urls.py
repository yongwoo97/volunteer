from django.contrib import admin
from django.urls import path, include
from authentication.views import registration_view, login_view, nickname_check, Activate
from board.views import chat_start_view


urlpatterns = [
    path('/', include('board.urls')),
    path('admin/', admin.site.urls),
    path('api/account/activate/<str:uidb64>/<str:token>', Activate.as_view()),
    path('api/register/', registration_view, name='register_user'),
    path('api/login/', login_view, name='login_user'),
    path('api/board/', include('board.urls')),
    path('api/nicknamecheck/', nickname_check, name='nickname_check'),
    path('api/chat/', include('chat.urls')),
    path('api/chatstart/', chat_start_view),
]


