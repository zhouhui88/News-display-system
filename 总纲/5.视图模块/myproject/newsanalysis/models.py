from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)


class news(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200,unique=True)
    time = models.CharField(max_length=50)
    source = models.CharField(max_length=500)
    digest = models.CharField(max_length=500)
    url = models.CharField(max_length=500)
    analysis = models.CharField(max_length=20)


class sina_weibo(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=500)
    date = models.CharField(max_length=200)
    star_num = models.IntegerField()
    rank = models.IntegerField()
    link = models.CharField(max_length=500)


class weibohot(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    date = models.CharField(max_length=100)
    star_num = models.IntegerField()
    rank = models.IntegerField()
    link = models.CharField(max_length=200)
    analysis = models.IntegerField()


class toutiao(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    source = models.CharField(max_length=200)
    abstruct = models.CharField(max_length=200)
    analysis = models.IntegerField()


class news163_fore(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200,unique=True)
    time = models.CharField(max_length=50)
    source = models.CharField(max_length=500)
    digest = models.CharField(max_length=500)
    url = models.CharField(max_length=500)
    analysis = models.CharField(max_length=20)


class news163_star(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200,unique=True)
    time = models.CharField(max_length=50)
    source = models.CharField(max_length=500)
    digest = models.CharField(max_length=500)
    url = models.CharField(max_length=500)
    analysis = models.CharField(max_length=20)

class news163_sport(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200,unique=True)
    time = models.CharField(max_length=50)
    source = models.CharField(max_length=500)
    digest = models.CharField(max_length=500)
    url = models.CharField(max_length=500)
    analysis = models.CharField(max_length=20)


class news163_stock(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200,unique=True)
    time = models.CharField(max_length=50)
    source = models.CharField(max_length=500)
    digest = models.CharField(max_length=500)
    url = models.CharField(max_length=500)
    analysis = models.CharField(max_length=20)


class news163_fund(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200,unique=True)
    time = models.CharField(max_length=50)
    source = models.CharField(max_length=500)
    digest = models.CharField(max_length=500)
    url = models.CharField(max_length=500)
    analysis = models.CharField(max_length=20)


class news163_tech(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200,unique=True)
    time = models.CharField(max_length=50)
    source = models.CharField(max_length=500)
    digest = models.CharField(max_length=500)
    url = models.CharField(max_length=500)
    analysis = models.CharField(max_length=20)


class news163_digit(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200,unique=True)
    time = models.CharField(max_length=50)
    source = models.CharField(max_length=500)
    digest = models.CharField(max_length=500)
    url = models.CharField(max_length=500)
    analysis = models.CharField(max_length=20)



class news163_era(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200,unique=True)
    time = models.CharField(max_length=50)
    source = models.CharField(max_length=500)
    digest = models.CharField(max_length=500)
    url = models.CharField(max_length=500)
    analysis = models.CharField(max_length=20)


class weibohot_count(models.Model):
    date = models.CharField(max_length=100)
    count = models.IntegerField()





































