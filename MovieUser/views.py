from django.contrib import messages, auth
from django.shortcuts import render, redirect
from django.contrib.auth.models import User


# Create your views here.

def login(request):
    if request.method == 'POST':
        username1 = request.POST.get('username')
        password1 = request.POST.get('password')
        context = {
            'has_error': False
        }

        user = auth.authenticate(username=username1, password=password1)
        print(user)
        if user is not None:
            request.session['uid'] = request.POST['username']
            if request.POST.get('remember_me'):
                response = redirect('/')
                response.set_cookie(
                    'cid', request.POST['username'], max_age=604800)
                response.set_cookie(
                    'cid2', request.POST['password'], max_age=604800)
                auth.login(request, user)
                messages.add_message(request, messages.SUCCESS,
                                     f'Welcome {user.username}')
                return response

            auth.login(request, user)
            messages.add_message(request, messages.SUCCESS,
                                 f'Welcome {user.username}')
            return redirect('/')

        else:
            messages.add_message(request, messages.ERROR, 'Invalid Login')
            context['has_error']: True
            return render(request, 'sign-in.html', context=context)

    else:
        if request.COOKIES.get('cid'):
            return render(request, 'sign-in.html', {'cookie1': request.COOKIES['cid'],
                                                    'cookie2': request.COOKIES['cid2']})
        return render(request, 'sign-in.html')


def signup(request):
    if request.method == 'POST':
        username1 = request.POST['username']
        firstname1 = request.POST['firstname']
        lastname1 = request.POST['lastname']
        email1 = request.POST['email']
        email = email1.lower()
        password = request.POST['password1']
        password1 = request.POST['password2']

        context = {
            'has_error': False
        }

        if firstname1 == '':
            messages.add_message(request, messages.ERROR,
                                 'Firstname is required')
            context['has_error']: True

        if lastname1 == '':
            messages.add_message(request, messages.ERROR,
                                 'Lastname is required')
            context['has_error']: True

        if password == '':
            messages.add_message(request, messages.ERROR,
                                 'Password is required')
            context['has_error']: True

        if password1 == '':
            messages.add_message(request, messages.ERROR,
                                 'Confirm Password is required')
            context['has_error']: True

        # password should match
        if password != password1:
            messages.add_message(request, messages.ERROR, 'Password Not Match')
            context['has_error'] = True

        if len(password) < 8:
            messages.add_message(request, messages.ERROR,
                                 'password shod be Atleast 8 character or more')
            context['has_error'] = True

        if context['has_error']:
            return render(request, 'sign-up.html', context, status=400)

        ''' Begin reCAPTCHA validation Only Work On Real Website'''
        # recaptcha_response = request.POST.get('g-recaptcha-response')
        # url = 'https://www.google.com/recaptcha/api/siteverify'
        # values = {
        #     'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
        #     'response': recaptcha_response
        # }
        # data = urllib.parse.urlencode(values).encode()
        # req = urllib.request.Request(url, data=data)
        # response = urllib.request.urlopen(req)
        # result = json.loads(response.read().decode())

        # if result['success']:
        #     user = User.objects.create_user(
        #         username=username1, email=email, password=password1)
        #     user.first_name = firstname1
        #     user.last_name = lastname1
        #     user.is_active = True
        #     user.save()
        #     messages.add_message(request, messages.SUCCESS,
        #                          'Account Successfully Created.')
        #     return render(request, 'userall/login.html')

        # else:
        #     messages.error(request, 'Invalid reCAPTCHA. Please try again.')
        #     return render(request, 'userall/register.html')

        ''' End reCAPTCHA validation '''

        user = User.objects.create_user(
            username=username1, email=email, password=password1)

        user.first_name = firstname1
        user.last_name = lastname1
        user.is_active = True
        user.save()

        messages.add_message(request, messages.SUCCESS,
                             'Account Successfully Created.')
        return render(request, 'sign-in.html')

    else:
        return render(request, 'sign-up.html')
