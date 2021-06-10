from django.shortcuts import render
from .models import *


# Create your views here.


def index(request):
    return render(request, 'index.html')


def movie_details(request):
    all_movie = Movie.objects.all().filter(M_latest='NOW')

    context = {
        'all_movie': all_movie
    }
    return render(request, 'movie-details.html', context)
