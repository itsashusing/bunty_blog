from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.


class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    bio=models.CharField(max_length=30)
    fb_url=models.CharField(max_length=50)
    image=models.ImageField(default='default.jpg',upload_to='profile_pic')

    def save(self):
        super().save()

        img= Image.open(self.image.path)

        if img.height >300 or img.width >300:
            output= (300,300)
            img.thumbnail(output)
            img.save(self.image.path)