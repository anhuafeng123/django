from django.db import models

# Create your models here.

from django.contrib.auth.models import  AbstractUser
from datetime import datetime

# Create your models here.
class BlogUser(AbstractUser):
    nikename = models.CharField(max_length=30,default='',verbose_name='昵称')

class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=50,verbose_name='验证码',default='')
    eamil = models.CharField(max_length=30,verbose_name='邮箱')
    send_type = models.CharField(max_length=30,verbose_name='验证码类型',choices=(('register','注册'),('forget','找回密码'),('uodate_email','修改邮箱')))
    send_time = models.DateTimeField(verbose_name='发送时间',default=datetime.now)

    class Meta:
        verbose_name = '邮箱验证'
        verbose_name_plural = verbose_name


    def __str__(self):
        return self.eamil
