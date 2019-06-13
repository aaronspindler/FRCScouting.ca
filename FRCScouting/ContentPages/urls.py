from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= 'home'),
    path('about/', views.about, name='about'),
    path('gamemanuals/', views.gamemanuals, name='gamemanuals'),
    path('privacy/', views.privacy, name='privacy'),
    path('licenses/', views.licenses, name='licenses'),
    path('contact/', views.contact, name='contact'),
]
