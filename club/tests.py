from django.test import TestCase
from .models import Meeting, MeetingMinutes, Resource, Event
from .forms import MeetingForm, ResourceForm

# Create your tests here.
class MeetingTest(TestCase):
    def setUp(self):
        self.type=Meeting(meetingtitle='company yearly earnings')
    
    def test_typestring(self):
        self.assertEqual(str(self.type), 'company yearly earnings')

    def test_tablename(self):
        self.assertEqual(str(Meeting._meta.db_table), 'meeting')
class MeetingMinutesTest(TestCase):
    def setUp(self):
        self.type=Meeting(meetingtitle='quarterly earnings meeting')
        self.minutes=MeetingMinutes(minutestext='30 minutes')

    def test_typestring(self):
        self.assertEqual(str(self.type), 'quarterly earnings meeting')
        self.assertEqual(str(self.minutes), '30 minutes')

    def test_tablename(self):
        self.assertEqual(str(MeetingMinutes._meta.db_table), 'meetingminutes')
class ResourceTest(TestCase):
    def setUp(self):
        self.type=Meeting(meetingtitle='quarterly earnings meeting')
        self.minutes=MeetingMinutes(minutestext='30 minutes')
        self.resource=Resource(resourcename='calculations from department')

    def test_typestring(self):
        self.assertEqual(str(self.type), 'quarterly earnings meeting')
        self.assertEqual(str(self.minutes), '30 minutes')
        self.assertEqual(str(self.resource), 'calculations from department')

    def test_tablename(self):
        self.assertEqual(str(Resource._meta.db_table), 'resource')

class EventTest(TestCase):
    def setUp(self):
        self.type=Meeting(meetingtitle='quarterly earnings meeting')
        self.minutes=MeetingMinutes(minutestext='30 minutes')
        self.resource=Resource(resourcename='calculations from department')
        self.event=Event(eventtitle='Tax season')

    def test_typestring(self):
        self.assertEqual(str(self.type), 'quarterly earnings meeting')
        self.assertEqual(str(self.minutes), '30 minutes')
        self.assertEqual(str(self.resource), 'calculations from department')
        self.assertEqual(str(self.event), 'Tax season')

    def test_tablename(self):
        self.assertEqual(str(Event._meta.db_table), 'event')

#Form tests
class MeetingForm_Test(TestCase):
    def test_typeform_is_valid(self):
        form=MeetingForm(data={'meetingname': "meeting1", "meetingdescription": "some meeting"})
        self.assertTrue(form.is_valid())

class ResourceForm_Test(TestCase):
    def test_typeform_is_valid(self):
        form=ResourceForm(data={'resourcename': "resource1"})
        self.assertEqual(form.is_valid())