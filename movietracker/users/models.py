from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth = models.DateField(blank=True)
    gender = models.CharField(max_length=1, choices=(('m', ('Male')), ('f', ('Female')), ('o', ('Non-Binary'))),blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} Profile"

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)