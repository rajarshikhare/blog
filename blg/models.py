from django.db import models
import time
from django.contrib.auth.models import User

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    facebook = models.CharField(max_length=300)
    twitter = models.CharField(max_length=300)
    instagram = models.CharField(max_length=300)
    email = models.CharField(max_length=1000, default='None')
    about = models.TextField(max_length=2000, default='Not given by the author but obviously he/she must be awesome!!s')

    def __str__(self):
        return self.name

class Topic(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    topic_name = models.CharField(max_length=200)
    abstract_img = models.CharField(max_length=200, default='None')
    abstract = models.CharField(max_length=1000, default='None')
    category = models.CharField(max_length=50, default='None')
    upload_date = models.CharField(max_length=50, default=time.ctime())
    link = models.CharField(max_length=200, default='None')
    content = models.TextField(max_length=10000, default='None')
    is_private = models.BooleanField(default=False)
    

    def __str__(self):
        return self.topic_name

class Comment(models.Model):
    cmt = models.TextField(max_length=300)
    writer_name = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    def __str__(self):
        return self.writer_name

class Client(models.Model):
    user_agent = models.CharField(max_length=1000)
    ip_address = models.CharField(max_length=20)
    time = models.CharField(max_length=100)
    city = models.CharField(max_length=100, default='None')
    country = models.CharField(max_length=100, default='None')
    isp = models.CharField(max_length=100, default='None')

    def __str__(self):
        return self.city + ' - ' + self.country  + ' - ' + self.isp


class WebsiteDetail(models.Model):
    about = models.TextField(max_length=500)
    twitter = models.CharField(max_length=100)
    facebook = models.CharField(max_length=100)
    instagram = models.CharField(max_length=100)
    contact = models.TextField(max_length=500, default='None')
    header = models.TextField(default='None')
    footer = models.TextField(default='None')

    def __self__(self):
        return self.about
