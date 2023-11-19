from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class User_Info(models.Model):
    user = models.OneToOneField(
        User, related_name="profile", on_delete=models.CASCADE, null=True)
    uid = models.CharField(max_length=50, null=False, default='')  # user_id
    name = models.CharField(max_length=255, blank=True, null=False)  # LINE名字
    pic_url = models.CharField(
        max_length=255, blank=False, null=False)  # 大頭貼網址
    notify_token = models.CharField(
        max_length=255, blank=True, null=True)  # Notify Access Token
    notification = models.BooleanField(default='False')
    mdt = models.DateTimeField(auto_now=True)  # 物件儲存的日期時間

    def __str__(self):
        return self.uid

    class Meta:
        db_table = 'Users'
        verbose_name_plural = '會員資料'
