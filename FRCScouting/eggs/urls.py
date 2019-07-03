from django.urls import path, include
from . import views

urlpatterns = [
    path('dog/', views.dog, name='eggs_dog'),
]
