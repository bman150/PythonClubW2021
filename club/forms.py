from django import forms
from .models import Meeting, Resource

# create the forms here
class MeetingForm(forms.ModelForm):
    # sub-classes
    class Meta:
        model=Meeting
        fields='__all__'

class ResourceForm(forms.ModelForm):
    #sub-classes
    class Meta:
        model=Resource
        fields='__all__'

class LoginForm(forms.ModelForm):
    #sub-classes
    class Meta:
        model=login
        fields='__all__'