from email.policy import default
from django.db import models
from users.models import User
#from django.contrib.auth.models import User
from datetime import datetime,date
# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=500)
    #image = models.ImageField(upload_to="blog/",default="avatar.png")
    image = models.ImageField(upload_to="blog",blank=True,null=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)
    likes= models.ManyToManyField(User,related_name="blog_posts")
    CATEGORY =(
        ("1","Frontend"),
        ("2","Backend"),
        ("3","FullStack"),
    )
    category = models.CharField(max_length=50, choices=CATEGORY)
    def __str__(self):
        return f"{self.title}"
    def number_of_likes(self):
        return self.likes.count()
# class Category(models.Model):
#     category = models.CharField(max_length=50, choices=CATEGORY)

class Comment(models.Model):
   post =  models.ForeignKey(Blog,related_name="comments",on_delete=models.CASCADE)   
   user=models.ForeignKey(User,on_delete=models.CASCADE)
   body= models.TextField()
   created_date = models.DateField(auto_now_add=True)
   
   
