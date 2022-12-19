from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import auth, User
from django.shortcuts import redirect
from .models import Cities
from random import randint as generator


# Create your views here.
def index(request):
    return render(request, 'landing.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['userName']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['passwordrepeat']

        if password == password2:
            if User.objects.filter(username=email).exists():
                messages.info(request, 'Email Already In Use')
                return redirect('signup')

            elif User.objects.filter(email=username).exists():
                messages.info(request, 'Username Already In Use, Try another one')
                return redirect('signup')

            elif username == "":
                messages.info(request, 'username can not be empty')
                return redirect('signup')

            else:
                user = User.objects.create_user(username=email, email=username, password=password,)
                user.save()
                luser = auth.authenticate(username=email, password=password)
                auth.login(request, luser)
                return redirect('home')

        else:
            messages.info(request, 'passwords does not match')
            return redirect('signup')
    else:
        return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(username=email, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')

        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('login')

    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def home(request):
    return render(request, 'home.html')


def fifty(request):
    return render(request, '50_must.html')


def search(request):
    if request.method == 'POST':
        citySearched = request.POST['city']
        query = []
        if Cities.objects.filter(cityName=str(citySearched).upper()).exists():
            query = Cities.objects.get(cityName=str(citySearched).upper())
            return render(request, 'search.html', {'city': query, 'num': 1, 'search': citySearched})
        else:
            query = None
            return render(request, 'search.html', {'city': query, 'num': 0, 'search': citySearched})
    else:
        return render(request, 'search.html')


def cities(request, city):
    if Cities.objects.filter(cityName=str(city).upper()).exists():
        query = Cities.objects.get(cityName=str(city).upper())
        return render(request, 'agra.html', {'city': query})
    else:
        return render(request, 'search.html')


def planner(request, city):
    if Cities.objects.filter(cityName=str(city).upper()).exists():
        query = Cities.objects.get(cityName=str(city).upper())
        return render(request, 'agra_planner.html', {'city': query})
    else:
        return render(request, 'search.html')


def about(request):
    return render(request, 'about.html')


def law(request):
    return render(request, 'law.html')


def suggest(request):
    if request.method == 'POST':
        city = ["AGRA",]
        suggest = city[generator(0, (len(city)-1))]
        if Cities.objects.filter(cityName=str(suggest).upper()).exists():
            query = Cities.objects.get(cityName=str(suggest).upper())
            return render(request, 'suggest.html', {'city': query, 'num': 1, 'search': suggest})
        else:
            query = None
            return render(request, 'suggest.html', {'city': query, 'num': 0, 'search': suggest})
    else:
        return render(request, 'suggest.html')

