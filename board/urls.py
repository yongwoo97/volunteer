from django.urls import path, include
from .views import boardviewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', boardviewset)

urlpatterns =[
    path('', include(router.urls)),
]