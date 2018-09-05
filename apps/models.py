from django.db import models

# Create your models here.


class UserInfo(models.Model):
    username = models.CharField(max_length=32, verbose_name='用户名')
    password = models.CharField(max_length=32, verbose_name='密码')
    email = models.EmailField(verbose_name='电子邮箱')
    city = models.CharField(max_length=32, verbose_name='城市')