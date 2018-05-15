from django.db import models

class Topic(models.Model):
    topic_name = models.CharField(max_length=200)
    abstract_img = models.CharField(max_length=200, default='None')
    abstract = models.CharField(max_length=1000, default='None')

    """
    algorithm_type = models.Charfield(max_length=50, default='None')
    """

    def __str__(self):
        return self.topic_name