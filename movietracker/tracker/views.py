from tracker.models import Movie
from django.shortcuts import render, redirect
from .models import *
from django.views.generic.detail import DetailView

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
                    movies = MovieStatus.objects.update(movie=film, user=user, status=status, favourite=favourite, rating=rating)
                    return redirect('movies')

        
        else:
            return render(request, 'tracker/top_movies.html')
                    


