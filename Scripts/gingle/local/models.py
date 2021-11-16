from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone
from django.contrib.auth import User

# Create your models here.
class Publication(models.Model):
    body = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)