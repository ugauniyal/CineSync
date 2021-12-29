from tracker.models import Movie
from django.shortcuts import render, redirect
from .models import *
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required

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


class MovieDetailView(DetailView):

    model = Movie

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            title = request.POST['movie']
            status = request.POST['status']
            favourite = bool(request.POST['favorite'])
            rating = request.POST['rating']
            user = request.user

            film = Movie.objects.get(title=title)



            if request.user.is_authenticated:
                if not MovieStatus.objects.filter(user = request.user, movie = film.id).exists():
                    movies = MovieStatus.objects.create(movie=film, user=user, status=status, favourite=favourite, rating=rating)
                    movies.save()
                    return redirect('movies')

                else:
                    movies = MovieStatus.objects.filter(user = request.user, movie = film.id).update(movie=film, user=user, status=status, favourite=favourite, rating=rating)
                    return redirect('movies')

        
        else:
            return render(request, 'tracker/top_movies.html')
                    

@login_required
def user_stats(request):

    stats = MovieStatus.objects.filter(user = request.user)
    watching = MovieStatus.objects.filter(user = request.user, status='Watching').count()
    plan_to_watch = MovieStatus.objects.filter(user = request.user, status='Plan to Watch').count()
    completed = MovieStatus.objects.filter(user = request.user, status='Completed').count()

    context = {'stats':stats, 'watching': watching, 'plan_to_watch': plan_to_watch, 'completed': completed}

    return render(request, 'tracker/user_stats.html', context=context)