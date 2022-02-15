from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True,null = True)
    bio = models.TextField(default=" ")
# class Profile(models.Model):
#     avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
#     bio = models.TextField()