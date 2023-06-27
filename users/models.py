from django.db import models
from django.contrib.auth.models import User #User model
from PIL import Image #pillow library for image resizing

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #if user is deleted, delete profile
    image = models.ImageField(default='default.jpg', upload_to='profile_pics') #upload_to is the directory where the image is stored

    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.image.path) #open image of current instance (users profile picture)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size) #resize image
            img.save(self.image.path) #save resized image to same path
            

