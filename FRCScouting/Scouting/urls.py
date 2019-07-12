from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('robot/add', views.robot_add, name='robot_add'),
    path('match', views.match_scouting, name='match_scouting'),
    path('pit', views.pit_scouting, name='pit_scouting'),
    #Stronghold
    #Steamworks
    #Powerup
    #Deep Space
    #Rise
]
