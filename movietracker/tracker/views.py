from tracker.models import Movie
from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    return render(request, 'tracker/homepage.html')



def contact(request):
    return render(request, 'tracker/contact_us.html')



def about(request):
    return render(request, 'tracker/about_us.html')


def movies(request):
    movie = Movie.objects.all()
    context = {'movie':movie}
    return render(request, 'tracker/top_movies.html', context)