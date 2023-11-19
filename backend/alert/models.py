from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Alerts(models.Model):
    user = models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
    title = models.TextField(null=True,blank=True)
    keyword = models.TextField(null=True,blank=True)
    area = models.TextField(null=True,blank=True)
    cat = models.TextField(null=True,blank=True)
    period = models.TextField(null=True,blank=True)
    salary = models.TextField(null=True,blank=True)
    class Meta:
        db_table = 'Alert'
        verbose_name_plural = '提醒'
    
    def __str__(self):
       return self.title