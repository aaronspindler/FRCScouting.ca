from django.urls import path
from . import views

urlpatterns = [
    path('teaminformation/', views.teaminformation, name='teaminformation'),
]
