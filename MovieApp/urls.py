from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('movie/<str:mDetails>/',
         movie_details, name='movie_details'),
    path('movie/<str:mDetails>/ticket-plan/',
         movie_seat_plan, name='movie_ticket_plan'),

    path('ajax/load-cities/', load_cities, name='ajax_load_cities'),
]
