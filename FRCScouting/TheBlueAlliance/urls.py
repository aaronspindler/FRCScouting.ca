from django.urls import path
from . import views

urlpatterns = [
    path('teaminfo/', views.teaminfo, name='tba_teaminfo'),
    path('teaminfo/<str:teamkey>/',views.teaminfodetails, name='tba_teaminfodetail'),
    path('eventinfo/', views.eventinfo, name='tba_eventinfo'),
    path('eventinfo/<str:eventkey>/',views.eventinfodetails, name='tba_eventinfodetail'),
    path('admin/controlpanel', views.admin_controlpanel, name='tba_admin_controlpanel'),
    path('admin/events/loaddata', views.events_loaddata, name='tba_admin_events_loaddata'),
    path('admin/teams/loaddata', views.teams_loaddata, name='tba_admin_teams_loaddata'),
]
