from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('movie/',
         movie_details, name='movie_details'),
]
