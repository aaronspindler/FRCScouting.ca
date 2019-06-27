from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= 'home'),
    path('about/', views.about, name='about'),
    path('gamemanuals/', views.gamemanuals, name='gamemanuals'),
    path('privacy/', views.privacy, name='privacy'),
    path('licenses/', views.licenses, name='licenses'),
    path('pitscouting/', views.pitscouting, name='pitscouting'),
    path('matchscouting/', views.matchscouting, name='matchscouting'),
    path('whyads/', views.whyads, name='why-ads'),
]
