from django.shortcuts import render
from  .models import Meeting, MeetingMinutes, Resource, Event

# Create your views here.
def index(request):
    return render(request, 'club/index.html')

def resources(request):
    resource_list_1=Resource.objects.all()
    resource_list_2=Meeting.objects.all()
    return render(request, 'club/resources.html', {'resource_list_1':resource_list_1, 'resource_list_2':resource_list_2})