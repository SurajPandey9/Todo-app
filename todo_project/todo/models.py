from django.db import models
from django.contrib.auth.models import AbstractUser

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
class CustomUser(AbstractUser):
    pass # Add additional fields if necessary
