from tracker.models import *
from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Movie)

admin.site.register(Category)

admin.site.register(Director)

admin.site.register(MovieStatus)