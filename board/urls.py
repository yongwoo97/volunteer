from django.urls import path, include
from .views import boardviewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', boardviewset)


print(type(include(router.urls)))
urlpatterns =[
    path('', include(router.urls)),
]

