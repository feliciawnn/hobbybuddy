from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Activity(models.Model):
    title = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='activity_media')
    description = models.TextField()
    cost_estimation = models.PositiveIntegerField()
