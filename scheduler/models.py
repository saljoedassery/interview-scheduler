from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    role = models.CharField(max_length=16)


class TimeSlot(models.Model):
    user = models.ForeignKey("CustomUser", blank=True, null=True, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f"{self.user.username}: {self.start_time} --> {self.end_time}"


