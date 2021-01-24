from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Meeting(models.Model):
    # fields
    meetingtitle=models.CharField(max_length=255)
    meetingdate=models.DateField()
    meetingtime=models.TimeField() # may need to edit this
    location=models.TextField(null=True, blank=True) # may need to edit
    agenda=models.TextField(null=True, blank=True) # may need to edit
    
    # methods
    def __str__(self):
        return self.meetingtitle

    # sub-classes
    class Meta:
        db_table='meeting'

class MeetingMinutes(models.Model):
    # fields
    meetingid=models.ForeignKey(Meeting, on_delete=models.DO_NOTHING)
    attendance=models.ManyToManyField(User)
    minutestext=models.TextField()

    # methods
    def __str__(self):
        return self.meetingid # may need to remove this or add additional field

    # sub-classes
    class Meta:
        db_table='meetingminutes'

class Resource(models.Model):
    # fields
    resourcename=models.CharField(max_length=255)
    resourcetype=models.TextField()
    url=models.URLField(null=True, blank=True) # may need to edit
    dateentered=models.DateField() # may need to edit as just DateField()
    userid=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    description=models.TextField(null=True, blank=True) # may need to edit

    # methods
    def __str__(self):
        return self.resourcename

    # sub-classes
    class Meta:
        db_table='resource'
        verbose_name_plural='resources'

class Event(models.Model):
    # fields
    eventtitle=models.CharField(max_length=255)
    location=models.TextField(null=True, blank=True) # may need to edit
    date=models.DateField()
    time=models.TimeField()
    description=models.TextField(null=True, blank=True) # may need to edit
    userid=models.ForeignKey(User, on_delete=models.DO_NOTHING)

    # methods
    def __str__(self):
        return self.eventtitle

    # sub-classes
    class Meta:
        db_table='event'
        verbose_name_plural='events'