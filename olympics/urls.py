from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('history', views.history, name='history'),
    path('hof', views.hall_of_fame, name='hall_of_fame'),
]

