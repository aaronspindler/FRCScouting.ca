from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('robot/add', views.robot_add, name='robot_add'),
]
