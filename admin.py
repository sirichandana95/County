from django.contrib import admin
from .models import Event, ContactUs, Hospital, HospDepartment, Patient
# Register your models here.


class EventList(admin.ModelAdmin):
    list_display = ('EventName', 'EventDescription', 'EventLocation', 'EventTimestamp')
    list_filter = ('EventName', 'EventTimestamp')
    search_fields = ('EventName',)
    ordering = ['EventName']

class ContactUsList(admin.ModelAdmin):
    list_display = ('contactId', 'firstName','lastName','emailId','question','created_date')
    list_filter = ('contactId', 'firstName','lastName','emailId','question','created_date')
    search_fields = ('contactId', 'firstName','lastName','emailId','question','created_date')
    ordering = ['contactId']

class HospitalList(admin.ModelAdmin):
    list_display = ( 'HospitalID', 'HospitalName', 'HospitalPhone' )
    list_filter = ( 'HospitalID', 'HospitalName')
    search_fields = ('HospitalName',)
    ordering = ['HospitalName']

class BedsAvailability(admin.ModelAdmin):
    list_display = ( 'HospitalName', 'Department', 'TotalBeds', 'BedsUsed', 'AvailableBeds' )
    #list_display = ('HospitalName', 'Department')
    list_filter = ( 'HospitalName', 'Department')
    search_fields = ('Department', )
    ordering = ['Department']

class PatientList(admin.ModelAdmin):
    list_display = ('PatientID','Status', 'HospitalName', 'FirstName', 'LastName', 'Gender', 'Date_of_Birth', 'Department', 'Injury_type', 'Condition_on_arrival', 'Room_No_If_Admitted', 'Kin_Name', 'Relationship_To_Victim',
                    'Triage_Tag_colour', 'Disposition_type', 'Disposition_time')
    list_filter = ('PatientID', 'HospitalName')
    search_fields = ('PatientID',)
    ordering = ['PatientID']

admin.site.register(Event, EventList)
admin.site.register(Patient, PatientList)
admin.site.register(ContactUs, ContactUsList)
admin.site.register(Hospital, HospitalList)
admin.site.register(HospDepartment, BedsAvailability)


