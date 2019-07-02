from django.conf.urls import url
from . import views
from django.urls import path
from django.contrib.auth.views import password_change as pwd_change, password_change_done as pwd_change_done, password_reset as reset, password_reset_done as reset_done, password_reset_confirm as reset_confirm, password_reset_complete as reset_complete


app_name = 'chs'

urlpatterns = [
    path('', views.home, name='home'),
    url(r'^$', views.home, name='home'),
    url(r'^home/$', views.home, name='home'),
    url(r'^contact_us/$', views.contact_us, name='contact_us'),
    url(r'^contact_us/thank_you', views.thank_you, name='thank_you'),
    #url(r'^thank_you/$', views.thank_you, name='thank_you'),


    #url(r'^admin_home/', views.admin_home, name='admin_home'),
    url(r'^admin_login/', views.admin_home, name='adminlogin'),
    url(r'^nurse_login/', views.nurse_home, name='nurselogin'),
    url(r'^password-change/done/$', pwd_change_done, name='password_change_done'),
    url(r'^password-change/$', pwd_change, {'post_change_redirect': '/password-change/done/'}, name='password_change'),
    url(r'^password-reset/complete/$', reset_complete, name='password_reset_complete'),
    url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$', reset_confirm, {'post_reset_redirect': '/password-reset/complete/'}, name='password_reset_confirm'),
    url(r'^password-reset/done/$', reset_done, name='password_reset_done'),
    url(r'^password-reset/$', reset, {'post_reset_redirect': '/password-reset/done/', 'email_template_name': 'registration/password_reset_email.html'}, name='password_reset'),
    url(r'^register/$', views.register, name='register'),
    url(r'^event_list/$', views.event_list, name='event_list'),
    url(r'^patient_list/$', views.patient_list, name='patient_list'),
    url(r'^bed_track/$', views.bed_track, name='bed_track'),
    url(r'^coordinator_home/$', views.coordinator_home, name='coordinator_home'),
    path('event/<int:pk>/edit/', views.event_edit, name='event_edit'),
    path('event/create/', views.event_new, name='event_new'),
    path('event/<int:pk>/delete/', views.event_delete, name='event_delete'),
    path('patient/<int:pk>/edit/', views.patient_edit, name='patient_edit'),
    path('patient/create/', views.patient_new, name='patient_new'),
    path('patient/<int:pk>/delete/', views.patient_delete, name='patient_delete'),
    path('patient/<int:pk>/summary/', views.patient_summary, name='patient_summary'),
    path('admin_home', views.admin_home, name='admin_home'),
    path('admin/users_list', views.users_list, name='users_list'),
    path('admin/nurse_list', views.nurse_list, name='nurse_list'),
    path('admin/coordinator_list', views.coordinator_list, name='coordinator_list'),
    path('admin/event_list', views.admin_event_list, name='admin_event_list'),
    path('admin/patient_list', views.admin_patient_list, name='admin_patient_list'),
    path('admin/user_option', views.user_option, name='user_option'),
    path('user/<int:pk>/edit/', views.user_edit, name='user_edit'),
    path('user/<username>/delete/', views.user_delete, name='user_delete'),
    path('user/create/', views.user_new, name='user_new'),
    path('nurse_home', views.nurse_home, name='nurse_home'),
    path('patient/<int:pk>/pdf/', views.patient_summary_pdf, name='patient_summary_pdf'),

    ]
