from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'tracker/homepage.html')



def contact(request):
    return render(request, 'tracker/contact_us.html')



def about(request):
    return render(request, 'tracker/about_us.html')