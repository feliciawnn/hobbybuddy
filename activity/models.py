from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Activity(models.Model):
    title = models.CharField(max_length=100)
    indoor = models.BooleanField(default=False)
    picture = models.ImageField(upload_to='activity_media')
    description = models.TextField()
    cost_estimation = models.PositiveIntegerField()

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class UserCategory(models.Model):
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, default=None, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "User Category"
        constraints = [models.UniqueConstraint(fields = ['user', 'category'], name = "unique user category")]

    def __str__(self):
        return str(self.user) + '-' + str(self.category)


class ActivityCategory(models.Model):
    activity = models.ForeignKey(Activity, default=None, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, default=None, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Activity Category"
        constraints = [models.UniqueConstraint(fields = ['activity', 'category'], name = "unique activity category")]

    def __str__(self):
        return str(self.activity) + '-' + str(self.category)