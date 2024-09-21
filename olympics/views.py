from django.shortcuts import render
from .models import Athlete


def index(request):
    return render(request, 'home.html')


def athlete(request, athlete_id):
    data = Athlete.objects.get(id=athlete_id)
    return render(request, 'athlete.html', {'athlete_data': data})


def history(request):
    return render(request, 'history.html')
