from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Users(models.Model):
    user_email = models.EmailField(max_length=254)
    user_name = models.CharField(max_length=30, primary_key=True)
    user_password = models.CharField(max_length=100)
    user_birth = models.DateTimeField('date published')
    user_sex = models.NullBooleanField()
    user_info = models.TextField()
    
    def __str__(self):
        return self.user_name


# Create your models here.
