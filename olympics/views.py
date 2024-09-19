from django.shortcuts import render


def index(request):
    return render(request, 'home.html')

def history(request):
    return render(request, 'history.html')
