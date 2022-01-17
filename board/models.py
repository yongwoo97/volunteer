from django.db import models
from django.conf import settings
from authentication.models import custom_user

# Create your models here.

class board(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    title = models.CharField(max_length=100)
    dday = models.CharField(max_length=200)
    members = models.IntegerField(default=0)
    part = models.CharField(max_length=100, null=False)
    zipcode = models.CharField(max_length=100, null=False)
    roadAddress = models.CharField(max_length=300, null=False)
    jibunAddress = models.CharField(max_length=300, null=False)
    detailAddress = models.CharField(max_length=300, null=False)
    officialname = models.CharField(max_length=100, null=False)
    belong = models.CharField(max_length=200, null=False)
    authentication = models.CharField(max_length=100, null=False)
    information = models.TextField(null=True)
    #picture 사진필드 작업중
    created_at = models.DateTimeField(auto_now_add=True)
    state = models.CharField(max_length=100, null=False)
    author = models.ForeignKey(custom_user, to_field='nickname', on_delete=models.CASCADE)
    counter = models.IntegerField(default=0)

    class Meta:
        # 데이터베이스에 저장될 때 저장되는 테이블이름
        db_table = 'board'
        ordering = ('id',)
