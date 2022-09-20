#--------Django Import--------#
from django.urls import path

#-------- Services Management View Import--------#
from .views import ComplainRegister
from user_management.views import (
    ComplaintDetailView,
    ComplaintUpdateView,
    ComplaintDeleteView,
    UserComplainListView,
    ComplainListView,
)
from django.contrib.auth.decorators import login_required

#-------- URL Pattern--------#
urlpatterns = [

    path('complain_register/',ComplainRegister.as_view(),name='complain-register'),
    path('home/',login_required(ComplainListView.as_view()),name='home-page'),
    path('user/<str:username>', UserComplainListView.as_view(), name='user-complain'),
    path('complaint/<int:pk>/', ComplaintDetailView.as_view(), name='Complaint-detail'),
    path('complaint/<int:pk>/update/', ComplaintUpdateView.as_view(), name='Complaint-update'),
    path('complaint/<int:pk>/delete/', ComplaintDeleteView.as_view(), name='Complaint-delete'),

]