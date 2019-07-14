from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('robot/add', views.robot_add, name='robot_add'),
    path('robots', views.robots, name='scouting_robots'),
    path('match', views.match_scouting, name='match_scouting'),
    path('pit', views.pit_scouting, name='pit_scouting'),
    #Stronghold
    #Steamworks
    #Powerup
    #Deep Space
    #Rise
]
