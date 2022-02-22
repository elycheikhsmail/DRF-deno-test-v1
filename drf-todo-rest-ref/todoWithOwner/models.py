from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TodoWithOwner(models.Model):
    text = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
