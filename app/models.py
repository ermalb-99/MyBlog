from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
     profile_image = models.ImageField(null=True,blank=True,upload_to='images/')
     user = models.OneToOneField(User,on_delete=models.CASCADE)
     bio = models.TextField()
     def __str__(self) -> str:
          return self.user.username.capitalize()
     



class TwitterPost(models.Model):
     content = models.TextField(max_length=250)
     author = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
     likes = models.IntegerField(User,blank=True,null=True)
     comments = models.TextField(editable=True,null=True,blank=True)
     date_created = models.DateTimeField(auto_now_add=True)
     image = models.ImageField(null=True, blank=True, upload_to='images/')

     def __str__(self) -> str:
          return str(self.content.capitalize())







