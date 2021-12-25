from django.contrib import admin
from django.urls import path, include
from authentication.views import registration_view, login_view



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/', registration_view, name='register_user'),
    path('api/login/', login_view, name='login_user'),
    path('api/', include('board.urls')),
]


