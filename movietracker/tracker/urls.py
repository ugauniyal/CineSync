from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import MovieDetailView


urlpatterns = [
    path("", views.home, name="home"),
    path("contact/", views.contact, name="contact"),
    path("about/", views.about, name="about"),
    path("movies/", views.movies, name="movies"),
    path("stats/", views.user_stats, name="stats"),
    path('movies/<int:pk>/', MovieDetailView.as_view(), name='movie-detail'),
]