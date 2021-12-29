from django import forms
from django.db import models
from django.forms import ModelForm
from .models import *


category_choices = Category.objects.all().values_list('name', 'name')
choice_list = [choice for choice in category_choices]

class MovieStatusForm(forms.ModelForm):
    class Meta:
        model = MovieStatus
        fields = ('status', 'favourite', 'rating')
        widgets = {
            'name': forms.Select(choices=choice_list, attrs={'class':'form-control'})
        }