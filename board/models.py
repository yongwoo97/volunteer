from django.db import models
from django.conf import settings
from authentication.models import custom_user

# Create your models here.


class board(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    title = models.CharField(max_length=100)
    author = models.ForeignKey(custom_user, to_field='nickname', null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    state = models.CharField(max_length=100, default='apply-state apply-ing')
    dday = models.CharField(max_length=100, null=False)
    members = models.IntegerField(default=0)
    part = models.CharField(max_length=50)
    place = models.CharField(max_length=300, null=False)
    detail = models.TextField(null=True)
