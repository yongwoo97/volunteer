# models.py
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

#hello
#또다른 수정사항입니다.
User = get_user_model()

class userType(models.TextChoices):
    bronzeType = 'BRONZE', 'Bronze'
    silverType = 'SILVER', 'Silver'
    platinumType = 'PLATINUM', 'Platinum'
    diamondType = 'DIAMOND', 'Diamond'


class UserRole(models.Model):
    userType = models.CharField(max_length=10,
        choices=userType.choices, default=userType.bronzeType)
    userForeignKey = models.OneToOneField(User, on_delete=models.CASCADE,
        null=True, blank=True, related_name='RoleUser')

    def __str__(self):
        return self.userForeignKey.username + ' / ' + self.userType + ' 등급'


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=False, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
        UserRole.objects.create(userForeignKey=instance)