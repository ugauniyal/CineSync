from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    type = models.CharField(max_length=64)

    class Meta:
        ordering = ('type',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.type



class Director(models.Model):
    name = models.CharField(max_length=64)
    birth = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    release = models.DateTimeField(default=timezone.now)
    rating = models.FloatField(default=0.0)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    director = models.ForeignKey(Director, on_delete=models.PROTECT, default=1)
    runtime = models.CharField(max_length=64, default="Not Specified")
    poster = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('movie')


class MovieStatus(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    status = models.CharField(max_length=64, choices=(('None', ('None')), ('Watching', ('Watching')), ('Plan to Watch', ('Plan To Watch')), ('Completed', ('Completed'))),blank=True, null=True)
    favourite = models.BooleanField(default=False)
    rating = models.FloatField(default=0.0)

    def __str__(self):
        return str(self.movie)