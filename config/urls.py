from django.contrib import admin
from django.urls import path
from authentication.views import registration_view, example_view, TokenAuthenticationView
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/register/', registration_view, name='register_user'),
    # path('api/auth/login/', obtain_auth_token, name='login'),
    path('api/auth/login/', TokenAuthenticationView.as_view(), name='login'),
    path('api/test/', example_view, name='example_view'),

]


