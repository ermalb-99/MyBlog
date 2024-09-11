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
     comments = models.TextField(editable=True,null=True,blank=True)
     date_created = models.DateTimeField(auto_now_add=True)
     image = models.ImageField(null=True, blank=True, upload_to='images/')
     likes = models.ManyToManyField(User,related_name='liked',default=None,blank=True)

     def __str__(self) -> str:
          return str(self.content.capitalize())
     @property
     def num_likes(self):
          return self.likes.all().count()
LIKE_CHOICES = (
     ('Like','Like'),
     ('Unlike','Unlike')
)
class Like(models.Model):
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     post = models.ForeignKey(TwitterPost, on_delete=models.CASCADE)
     value = models.CharField(choices=LIKE_CHOICES,default='Like',max_length=10)

     def __str__(self) -> str:
          return str(self.post)




