from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('history', views.history, name='history'),
    path('leader', views.leaderboard, name='leaderboard'),
    path('hof', views.hall_of_fame, name='hall_of_fame'),
    path('athlete_list', views.athlete_list, name='athlete_list'),
]

