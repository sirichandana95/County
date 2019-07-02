from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import date
# Create your models here.

class ContactUs(models.Model):
    contactId = models.AutoField(null=False, primary_key=True)
    firstName = models.CharField(max_length= 100)
    lastName = models.CharField(max_length=100)
    emailId = models.CharField(max_length=50)
    question = models.TextField()
    created_date = models.DateField(default=timezone.now)

    def __str__(self):
        self.save()
        self.created_date = timezone.now()
        return str(self.contactId)

Injurylevel = (
    ('good/fair', 'Good/Fair'),
    ('serious', 'Serious'),
    ('critical', 'Critical'),
    ('expired', 'Expired'),
)


class Event(models.Model):
    EventID = models.IntegerField(null=False, primary_key=True)
    EventName = models.CharField(max_length=100, blank=True)
    EventDescription = models.CharField(max_length=100)
    EventTimestamp = models.DateTimeField(default=timezone.now)
    EventLocation = models.CharField(max_length=100)
    InjuryLevel = models.CharField(max_length=10, choices=Injurylevel, default='good/fair')
    NumberofPatients = models.IntegerField()
    #CoordinatorName = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='events', default='')
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.EventName)



class Hospital(models.Model):
    HospitalID = models.IntegerField(primary_key=True)
    HospitalName = models.CharField(max_length=100)
    HospitalAddress = models.CharField(max_length=200)
    HospitalCity = models.CharField(max_length=50)
    HospitalState = models.CharField(max_length=50)
    HospitalZipcode = models.CharField(max_length=10)
    HospitalPhone = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.HospitalName)


Department = (
    ('ICU/CC', 'ICU/CC'),
    ('ER', 'ER'),
    ('Med/Surg', 'Med/Surg'),
    ('OB', 'OB'),
    ('SICU', 'SICU'),
    ('Neg_Pres_Iso', 'Neg Pres/Iso'),
    ('OR', 'OR'),
    ('Peds', 'Peds'),
    ('PICU', 'PICU'),
    ('NICU', 'NICU'),
    ('Burn', 'Burn'),
    ('Mental Health', 'Mental Health'),
    ('Other', 'Other'),
)

class HospDepartment(models.Model):
    HospitalName = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name='HospDepartment')
    Department = models.CharField(max_length=50, choices=Department, default='ICU/CC')
    TotalBeds = models.IntegerField()
    BedsUsed = models.IntegerField()
    AvailableBeds = models.IntegerField()
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    #def bedsavailable(self):
        #return self.TotalBeds - self.BedsUsed
        # self.save()

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.HospitalName)

Gender = (
    ('Female', 'Female'),
    ('Male', 'Male'),
    ('Others', 'Others'),
)

Injury_type = (
    ('Cuts', 'Cuts'),
    ('Strains/Sprains', 'Strains/Sprains'),
    ('Burns', 'Burns'),
    ('Abrasions', 'Abrasions'),
    ('Internal Injuries', 'Internal Injuries'),
    ('Fractures', 'Fractures'),
    ('Respiratory Conditions', 'Respiratory Conditions'),
    ('Others', 'Others'),
)

Relationship_To_Victim = (
    ('Wife', 'Wife'),
    ('Mother', 'Mother'),
    ('Father', 'Father'),
    ('Husband', 'Husband'),
    ('Daughter', 'Daughter'),
    ('Son', 'Son'),
    ('Others', 'Others'),
)
Condition_on_arrival = (
    ('good/fair', 'Good/Fair'),
    ('serious', 'Serious'),
    ('critical', 'Critical'),
    ('expired', 'Expired'),
)

Triage_Tag_colour = (
    ('Green', 'Green'),
    ('Yellow', 'Yellow'),
    ('Red', 'Red'),
    ('Black', 'Black'),
)

Disposition_type = (
    ('To home', 'To home'),
    ('Other Hospital', 'Other Hospital'),
    ('SNF', 'SNF'),
    ('ICF', 'ICF'),

)
status=(('Active','Active'),('Inactive','Inactive'))
class Patient(models.Model):
    PatientID = models.IntegerField(primary_key=True)
    Status=models.CharField(max_length=20, choices=status, default='')
    HospitalName = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name='Patient')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Patient', default='')
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    Date_of_Birth = models.DateTimeField(default=timezone.now)
    Injury_type = models.CharField(max_length=10, choices=Injury_type)
    Condition_on_arrival = models.CharField(max_length=10, choices=Condition_on_arrival)
    Triage_Tag_colour = models.CharField(max_length=10, choices=Triage_Tag_colour)
    Department = models.CharField(max_length=50, choices=Department)
    Gender = models.CharField(max_length=10, choices=Gender)
    Room_No_If_Admitted = models.IntegerField(default='')
    Kin_Name = models.CharField(max_length=100)
    Relationship_To_Victim = models.CharField(max_length=10, choices=Relationship_To_Victim)
    Disposition_type = models.CharField(max_length=50, choices=Disposition_type)
    Disposition_time = models.DateTimeField(default=timezone.now)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def dob(self):
        self.Date_of_Birth = timezone.now()
        self.save()
    def Dispostiontime(self):
        self.Disposition_time = timezone.now()
        self.save()

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.PatientID)

