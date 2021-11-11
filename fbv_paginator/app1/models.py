from django.db import models

# Create your models here.
class Article(models.Model):

    aid = models.IntegerField()
    article = models.TextField()

    