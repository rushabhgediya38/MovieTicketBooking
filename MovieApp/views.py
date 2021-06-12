from django.shortcuts import render, HttpResponse
from .models import *


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


def movie_details(request, mDetails):
    all_movie = Movie.objects.all().filter(name=mDetails)

    context = {
        'all_movie': all_movie
    }
    return render(request, 'movie-details.html', context)


# def movie_details_example(request):
#     all_movie = Movie.objects.all().filter(M_latest='NOW')
#
#     context = {
#         'all_movie': all_movie
#     }
#     return render(request, 'movie-details.html', context)

def movie_seat_plan(request, mDetails):
    movie_available = Movie.objects.all().filter(name__exact=mDetails)
    states = M_state.objects.all().order_by('st_name')
    if movie_available:
        print('-------------------------', movie_available)
        context = {
            'movie_av': movie_available,
            'state': states
        }
        return render(request, 'movie-ticket-plan.html', context)
    else:
        return HttpResponse('movie not find')


def load_cities(request):
    state_id = request.GET.get('state')
    cities = M_city.objects.filter(m_state_id=state_id)
    print('-------------All-Cities-----------------', cities)
    return render(request, 'dropdownFolder/city_dropdown_list_options.html', {'cities': cities})


def load_multiplex(request):
    city_id = request.GET.get('city')
    M_name = request.GET.get('M_name')

    multi = M_multiplex_name.objects.filter(m_city_name_id=city_id, Multiplex_movie__name__exact=M_name)

    # print('-------------All-Multiplex-----------------', multi)
    print('-------------All-Multiplex-movie name-----------------', M_name)
    return render(request, 'dropdownFolder/multiplex_dropdown.html', {'multi': multi})


def load_exp(request):
    multiplexName = request.GET.get('cinema')
    print('-------------All-exp-----------------', multiplexName)

    check_name = M_multiplex_name.objects.filter(multiplex_name__exact=multiplexName)
    print(check_name)
    return render(request, 'dropdownFolder/user_view.html', {'view': check_name})
