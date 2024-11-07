import csv
import os
import pycountry
from django.core import serializers
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render
from .models import Athlete, Highlight


def index(request):
    return render(request, 'home.html')


def athlete(request, athlete_id):
    data = Athlete.objects.get(id=athlete_id)
    return render(request, 'athlete.html', {'athlete_data': data})


def hall_of_fame(request):
    data = Athlete.objects.all()
    countries = Athlete.objects.values('country').distinct()
    sports = Athlete.objects.values('sport').distinct()
    return render(request, 'hall_of_fame.html',
                  {'countries': [(x['country'], pycountry.countries.get(alpha_2=x['country']).name) for x in
                                 countries],
                   'sports': [x['sport'] for x in sports]})


def athlete_list(request):
    if request.method == 'POST':
        print(request.POST)
        countries = request.POST.getlist('country[]')
        sports = request.POST.getlist('sport[]')
        name = request.POST.get('name')
        print(name)
        if not countries and not sports and not name:
            data = Athlete.objects.all()
        else:
            # Dynamic filtering according to user input
            data = Athlete.objects.all()
            if countries:
                c_query = Q()
                for country in countries:
                    c_query |= Q(country=country)
                data = data.filter(c_query)

            if sports:
                s_query = Q()
                for sport in sports:
                    s_query |= Q(sport__contains=sport)
                data = data.filter(s_query)

            if name:
                data = data.filter(name__contains=name)

        return JsonResponse({'athletes': serializers.serialize('json', data)})


def leaderboard(request):
    here = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(here, 'olympics2024.csv')
    countries = []
    with open(filename, "r") as f:
        reader = csv.reader(f)
        data = list(reader)

        for row in data[1:]:
            # resolve country alpha 3 code to alpha 2 code and full name, and add to list
            if not pycountry.countries.get(alpha_3=row[2]):
                print(row[1])
                countries.append((row[0], row[1], None, row[3], row[4], row[5], row[6]))
            else:
                countries.append(
                    (row[0], row[1], pycountry.countries.get(alpha_3=row[2]).alpha_2, row[3], row[4], row[5], row[6]))
    return render(request, 'leaderboard.html', {'countries': countries})


def history(request):
    return render(request, 'history.html')


def highlights(request):
    return render(request, 'highlights.html', {'highlights': Highlight.objects.all()})
