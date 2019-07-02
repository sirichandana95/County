from django import forms
from .models import ContactUs, Event, Patient, HospDepartment
from django.contrib.auth.models import User
from django.forms.widgets import DateInput


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ('firstName', 'lastName', 'emailId', 'question',)

class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(widget=forms.PasswordInput)

class HospDepartmentForm(forms.Form):
    class Meta:
        model = HospDepartment
        fields = ('HospitalName', 'Department')

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        #exclude = ('user',)
        fields = ('EventID', 'EventName', 'EventDescription', 'EventTimestamp', 'EventLocation', 'InjuryLevel', 'NumberofPatients', 'user')


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username')

class PatientForm(forms.ModelForm):
    # Date_of_Birth=forms.DateField(input_formats=settings.DATE_INPUT_FORMATS['%d-%m-%Y'])
    class Meta:
        model = Patient
        #exclude = ('user',)
        fields = ('PatientID','Status', 'HospitalName', 'FirstName', 'LastName', 'Date_of_Birth', 'Gender', 'Department', 'Injury_type', 'Condition_on_arrival', 'Room_No_If_Admitted', 'Kin_Name', 'Relationship_To_Victim',
                    'Triage_Tag_colour', 'Disposition_type', 'Disposition_time')
        widgets={'Date_of_Birth': DateInput(attrs={'type':'date'}),
                 'Disposition_time': DateInput(attrs={'type':'date'}),
                 }