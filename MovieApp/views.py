from django.shortcuts import render
from .models import *


# Create your views here.


def index(request):
    all_now = Movie.objects.all().filter(M_latest='NOW')
    print(all_now)
    all_ex = Movie.objects.all().filter(M_latest='EXCLUSIVE')
    all_co = Movie.objects.all().filter(M_latest='COMING')

    context = {
        'm_now': all_now,
        'm_ex': all_ex,
        'm_co': all_co
    }
    return render(request, 'index.html', context)


def movie_details(request):
    all_movie = Movie.objects.all().filter(M_latest='NOW')

    context = {
        'all_movie': all_movie
    }
    return render(request, 'movie-details.html', context)
