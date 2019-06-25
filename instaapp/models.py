from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    profile_photo = models.ImageField(upload_to='avatar/')
    bio = models.TextField()
  

    def __str__(self):
        return self.bio
    def save_profile(self):
        self.save()
    
    def delete_profile(self):
        self.delete()


class Post(models.Model):
    image = models.ImageField(upload_to='instaapp/')
    image_name = models.CharField(max_length=40)
    image_caption = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.image_name

    def save_image(self):
        self.save()
    
    def delete_image(self):
        self.delete()
    
    @classmethod
    def get_images(cls):
        all_images = cls.objects.all()
        return all_images
    
class Comment(models.Model):
   image = models.ForeignKey('Post')
   user = models.ForeignKey(User)
   comment = models.CharField(max_length=100)

  