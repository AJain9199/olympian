from django.shortcuts import render
from .models import Athlete


def index(request):
    return render(request, 'home.html')


def athlete(request, athlete_id):
    data = Athlete.objects.get(id=athlete_id)
    return render(request, 'athlete.html', {'athlete_data': data})


def hall_of_fame(request):
    data = Athlete.objects.all()
    return render(request, 'hall_of_fame.html', {'athletes': [data[i * 3:(i + 1) * 3] for i in range((len(data) + 2) // 3 )]})

def history(request):
    return render(request, 'history.html')
