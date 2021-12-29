from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth = models.DateField(blank=True)
    image = models.ImageField(default='deafult.jpg', upload_to='profile_pics')
    bio = models.TextField(default='Not Specified')
    gender = models.CharField(max_length=10, choices=(('Male', ('Male')), ('Female', ('Female')), ('Non-Binary', ('Non-Binary'))),blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} Profile"

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)