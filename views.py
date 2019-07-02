from .forms import *
from .models import *
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.utils import timezone
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404
from django.db.models import Count

def home(request):
    return render(request, 'chs/home.html',
                  {'chs': home})



def adminlogin(request):

    if request.user.is_staff:
        return redirect('chs/nurse_login.html')
    else:
        return redirect('chs/admin_login.html')


def contact_us(request):
   if request.method == "POST":
       form = ContactForm(request.POST)
       if form.is_valid():
           contact = form.save(commit=False)
           contact.save()
           contacts = ContactUs.objects.filter(created_date=timezone.now())
           return render(request, 'chs/contact_us.html',
                         {'contacts': contacts})
   else:
       form = ContactForm()
       # print("Else")
   return render(request, 'chs/contact_us.html', {'form': form})


def thank_you(request):
    return render(request, 'chs/thank_you.html',
                  {'thank_you': thank_you})


@permission_required('is_staff')
def admin_home(request):

    return render(request, 'chs/admin_home.html',
                  {'chs': admin_home})



def admin_login(request):
    return render(request, 'chs/admin_login.html', {'chs': admin_login})
     # return HttpResponseRedirect('admin_login')


@login_required
def event_list(request):
    event = Event.objects.filter()
    return render(request, 'chs/event_list.html',
                 {'event': event})

#@login_required
def bed_track(request):
    if request.method == "POST":
        form = HospDepartmentForm(request.POST)
    hospdepartment = HospDepartment.objects.filter()
    for x in hospdepartment:
        p = Patient.objects.filter(HospitalName=x.HospitalName, Department=x.Department, Status='Active').aggregate(Count('PatientID')).values()
        for pa in p:
            x.BedsUsed = pa
            x.AvailableBeds = x.TotalBeds-x.BedsUsed
            x.save()
    hospdepartment1 = HospDepartment.objects.filter()
    return render(request, 'chs/bed_track.html', {'hospdepartment1': hospdepartment1})

def coordinator_home(request):
   return render(request, 'chs/coordinator_home.html', {'coordinator_home': coordinator_home})

def event_edit(request, pk):
   event = get_object_or_404(Event, pk=pk)
   if request.method == "POST":
       form = EventForm(request.POST, instance=event)
       if form.is_valid():
           event = form.save()
           # service.customer = service.id
           event.updated_date = timezone.now()
           event.user = request.user
           event.save()
           event = Event.objects.filter()
           return render(request, 'chs/event_list.html', {'event': event})
   else:
       # print("else")
       form = EventForm(instance=event)
   return render(request, 'chs/event_edit.html', {'form': form})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
            user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'chs/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
        return render(request, 'chs/register.html', {'user_form': user_form})

@login_required
def event_new(request):
   if request.method == "POST":
       form = EventForm(request.POST)
       if form.is_valid():
           event = form.save(commit=False)
           event.created_date = timezone.now()
           event.username = request.user
           event.save()
           event = Event.objects.filter()
           return render(request, 'chs/event_list.html',
                         {'event': event})
   else:
       form = EventForm()
       # print("Else")
   return render(request, 'chs/event_new.html', {'form': form})

def event_delete(request, pk):
   event = get_object_or_404(Event, pk=pk)
   event.delete()
   return redirect('chs:event_list')


@permission_required('is_superuser')
def admin_home(request):
    return render(request, 'chs/admin_home.html',
                  {'admin': admin_home})

@login_required
def nurse_home(request):
    return render(request, 'chs/nurse_home.html',
                  {'nurse': nurse_home})

@login_required
def users_list(request):
    users = User.objects.all()
    #print(users)
    return render(request, 'chs/users_list.html', {'users': users})

@login_required
def user_option(request):
    return render(request, 'chs/user_option.html',
                 {'admin': user_option})

@login_required
def nurse_list(request):
    #users = User.objects.filter(groups=2)
    users = User.objects.filter(groups__name='Nurse')
    #user = Group.objects.get(name="Nurse")
    return render(request, 'chs/nurse_list.html',{'users': users})

@login_required
def coordinator_list(request):
    #users = User.objects.filter(groups=3)
    users = User.objects.filter(groups__name='Co-ordinator')
    #user = Group.objects.get(name="Nurse")
    return render(request, 'chs/coordinator_list.html',{'users': users})

@login_required
def user_edit(request, pk):
   user = get_object_or_404(User, pk=pk)
   #useredit = User.objects.get(username=username)
   if request.method == "POST":
       # update
       form = UserEditForm(request.POST, instance=user)
       if form.is_valid():
           user = form.save(commit=False)
           user.updated_date = timezone.now()
           user.save()
           #users = User.objects.filter(updated_date__lte=timezone.now())
           users = User.objects.filter()
           print(users)
           return render(request, 'chs/users_list.html',
                         {'users': users})
   else:
        # edit
       form = UserEditForm(instance=user)
       return render(request, 'chs/user_edit.html', {'form': form})

@login_required
def user_delete(request, username):
    users = User.objects.get(username=username)
    #print(request.user)
    #print(users)
    #print(User.objects.get(username='admin1').pk)
    #users = get_object_or_404(User, pk=pk)
    users.delete()
    return redirect('chs:users_list')
    #users = User.objects.all()
    #return render(request, 'chs/users_list.html', {'users': users})

@login_required
def user_new(request):
   if request.method == "POST":
       form = UserEditForm(request.POST)
       if form.is_valid():
           newuser = form.save(commit=False)
           newuser.date_joined = timezone.now()
           newuser.save()
           users = User.objects.filter(date_joined__lte=timezone.now())
           return render(request, 'chs/users_list.html',
                         {'users': users})
   else:
       form = UserEditForm()
       # print("Else")
   return render(request, 'chs/user_new.html', {'form': form})

@login_required
def admin_event_list(request):
    event = Event.objects.filter()
    return render(request, 'chs/admin_event_list.html',
                 {'event': event})
@login_required
def admin_event_list(request):
    event = Event.objects.filter()
    return render(request, 'chs/admin_event_list.html',
                 {'event': event})
@login_required
def admin_patient_list(request):
    patient = Patient.objects.filter()
    return render(request, 'chs/admin_patient_list.html',
                 {'patient': patient})
@login_required
def patient_list(request):
    patient = Patient.objects.filter()
    return render(request, 'chs/patient_list.html',
                 {'patient': patient})

def patient_edit(request, pk):
   patient = get_object_or_404(Patient, pk=pk)
   if request.method == "POST":
       form = PatientForm(request.POST, instance=patient)
       if form.is_valid():
           patient = form.save()
           # service.customer = service.id
           patient.updated_date = timezone.now()
           patient.user = request.user
           patient.save()
           patient = Patient.objects.filter()
           return render(request, 'chs/patient_list.html', {'patient': patient})
   else:
       # print("else")
       form = PatientForm(instance=patient)
   return render(request, 'chs/patient_edit.html', {'form': form})

@login_required
def patient_new(request):
   if request.method == "POST":
       form = PatientForm(request.POST)
       if form.is_valid():
           patient = form.save(commit=False)
           patient.created_date = timezone.now()
           patient.user = request.user
           patient.save()
           patient = Patient.objects.filter()
           return render(request, 'chs/patient_list.html',
                         {'patient': patient})
   else:
       form = PatientForm()
       # print("Else")
   return render(request, 'chs/patient_new.html', {'form': form})

def patient_delete(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    patient.delete()
    return redirect('chs:patient_list')

@login_required
def patient_summary(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    # patient = Patient.objects.filter(created_date__lte=timezone.now())
    patient = Patient.objects.filter(PatientID=pk)
    return render(request, 'chs/patient_summary.html', {'patient': patient})

from django.http import HttpResponse
from django.template.loader import get_template
from easy_pdf.rendering import render_to_pdf
from django.views.generic import View

@login_required
#class _summary_pdf(View):
def patient_summary_pdf(request, pk):
    template = get_template('chs/patient_summary_pdf.html')
    patient = get_object_or_404(Patient, pk=pk)
    #patient = Patient.objects.filter(created_date__lte=timezone.now())
    patients = Patient.objects.filter(PatientID=pk)
    context = {'patient': patient,}
    html = template.render(context)

    # 'email_success': email_success})
    pdf = render_to_pdf('chs/patient_summary_pdf.html', context)
    if pdf:
        response = HttpResponse(pdf, content_type='application/patient_summary_pdf')
        filename = 'patient_Summary_'+str(Patient.PatientID)+'.pdf'
        content = "inline; filename='%s'" % (filename)
        download = request.GET.get("download")
        if download:
            content = "attachment; filename='%s'" % (filename)
        response['Content-Disposition'] = content
        return response
    return HttpResponse("not found")

@login_required
def patient_summary_generate_pdf(request, pk, context):
    patient = get_object_or_404(Patient, pk=pk)
    template = get_template('chs/patient_summary_pdf.html')
    html = template.render(context)
    pdf = render_to_pdf('chs/patient_summary_pdf.html', context)
    if pdf:
        response =HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'filename= "summary{}.pdf"'.format(patient.PatientID)
        #return response
        #return HttpResponse(pdf, content_type='application/octet-stream')
        return pdf
    return HttpResponse("Not Found")


