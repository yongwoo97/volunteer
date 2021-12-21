from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class custom_user(models.Model):
    email = models.EmailField(max_length=100, unique = True)
    password1 = models.CharField(max_length=200)
    password2 = models.CharField(max_length=200)
    username = models.CharField(max_length=100)

    #봉사기관(True) or 봉사자(False)
    purpose = models.BooleanField(default=False)
    #소속
    belong = models.CharField(max_length=300, default=None)

    class Meta:
        #데이터베이스에 저장될 때 저장되는 테이블이름
        db_table = 'accounts'

    def __str__(self):
        return self.email

@receiver(post_save, sender = settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance = False, created=False, **kwargs):
    if created:
        Token.objects.create(user = instance)