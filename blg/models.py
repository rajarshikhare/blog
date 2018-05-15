from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=200)
    facebook = models.CharField(max_length=300)
    twitter = models.CharField(max_length=300)
    instagram = models.CharField(max_length=300)
    img_url = models.CharField(max_length=1000, default='None')
    about = models.CharField(max_length=2000, default='Not given by the author but obviously he/she must be awesome!!s')

    def __str__(self):
        return self.name

class Topic(models.Model):
    author = models.CharField(max_length=200, default='None')
    topic_name = models.CharField(max_length=200)
    abstract_img = models.CharField(max_length=200, default='None')
    abstract = models.CharField(max_length=1000, default='None')
    algorithm_type = models.CharField(max_length=50, default='None')
    upload_date = models.CharField(max_length=50, default='None')
    

    def __str__(self):
        return self.topic_name
