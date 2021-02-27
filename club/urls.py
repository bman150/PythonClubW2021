from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('resources/', views.resources, name='resources'),
    path('getmeetings/', views.getmeetings, name='meetings'),
    path('meetingdetails/', views.meetingdetails, name='meetingdetails'),
    path('newMeeting/', views.newMeeting, name='newmeeting'),
    path('newResource/', views.newResource, name='newresource'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]