#--------django default imports--------#

from os import stat
from re import template
from django.contrib import admin
from django.urls import path, include
admin.site.site_header="Shiv Shiva Residency "
#--------View import--------#

from user_management.views import Contact_form_detail,User_Profile_DetailView
from user_management import views as user_views


#--------Lgoin & Logout--------#
from django.contrib.auth import views as auth_views

#--------For Media Static Files--------#
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',user_views.index,name='index-page'), 

    # -------- Register Price & Contact Form -------- #

    path('contact_form/',Contact_form_detail.as_view(),name='contact-form'),
    path('price/',user_views.pricing,name='room-price'),   
    path('register/',user_views.register,name='register'),

    # -------- Profile Management -------- #

    path('profile/', user_views.profile, name='profile'),

    #-------- user profile for pharamacy detail view ------- #
    path('user_profile/<id>/', User_Profile_DetailView,name='user-profile-detail'),
    
    

    #-------- Login Logout system -------- #

    path('login/',auth_views.LoginView.as_view(template_name='user_management/login.html'),name='Login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='user_management/logout.html'),name='Logout'),

    #-------- App Url Include -------- #

    path('service/', include('services_management.urls')),
    path('user/user_request/', include('user_request.urls')),
    path('user/', include('room_management.urls')),
    path('pharmacy_request_Register/', include('pharmacy_management.urls')),

]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)