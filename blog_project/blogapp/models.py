from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=100)
    body=models.TextField()
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateTimeField(default=timezone.now)
    like=models.ManyToManyField(User,related_name='like',blank=True)

    def Total_like(self):
        return self.like.count()
    
class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    comment_text=models.TextField()