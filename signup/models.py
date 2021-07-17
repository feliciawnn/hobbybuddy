from django.db import models
from django.contrib.auth.models import User
from activity.models import Activity

# Create your models here.

class UserActivity(models.Model):
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, default=None, on_delete=models.CASCADE)
    class Meta:
        verbose_name = "User Activity"
        constraints = [models.UniqueConstraint(fields = ['user', 'activity'], name = "unique user activity")]
    def __str__(self):
        return str(self.user)+'-'+str(self.activity)
