from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
    path('logout', views.logout, name='logout'),
    path('profile/', views.profile, name='profile')
]