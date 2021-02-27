from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from  .models import Meeting, MeetingMinutes, Resource, Event
from .forms import MeetingForm, ResourceForm, LoginForm

# Create your views here.
def index(request):
    return render(request, 'club/index.html')

def resources(request):
    resource_list_1=Resource.objects.all()
    resource_list_2=Meeting.objects.all()
    return render(request, 'club/resources.html', {'resource_list_1':resource_list_1, 'resource_list_2':resource_list_2})

def getmeetings(request):
    meetings_list=Meeting.objects.all()
    return render(request, 'club/getmeetings.html', {'meetings_list': meetings_list})

def meetingdetails(request, id):
    meet=get_object_or_404(Meeting, pk=id)
    name=meet.meetingtitle
    date=meet.meetingdate
    time=meet.meetingtime
    locations=meet.location
    agendas=meet.agenda
    context={
        'meet' : meet,
        'name' : name,
        'date' : date,
        'time' : time,
        'locations' : locations,
        'agendas' : agendas,
    }
    return render(request, 'club/meetingdetails.html', context=context)

@login_required
def newMeeting(request):
    form=MeetingForm
    if request.method=='POST':
        form=MeetingForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=MeetingForm()
    else:
        form=MeetingForm()
    return render(request, 'club/newmeeting.html', {'form': form})

@login_required
def newResource(request):
    form=ResourceForm
    if request.method=='POST':
        form=ResourceForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=ResourceForm()
    else:
        form=ResourceForm()
    return render(request, 'club/newresource.html', {'form': form})

#Create login and logout view
def login(request):
    return render(request, 'club/login.html')

def logout(request):
    return render(request, 'club/logout.html')