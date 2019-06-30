from django.urls import path
from . import views

urlpatterns = [
    path('teaminfo/', views.teaminfo, name='tba_teaminfo'),
    path('teaminfo/<str:teamkey>/',views.teaminfodetails, name='tba_teaminfodetail'),
    path('eventinfo/', views.eventinfo, name='tba_eventinfo'),
]
