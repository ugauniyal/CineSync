from django.db import models
from django.utils import timezone
from django.urls import reverse

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

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('movie')