#-------- Django Import--------#

from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import  reverse_lazy

#-------- Staff Decorator Logic --------#
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator

#-------- Form Import --------#
from .forms import Room_Management_Form,User_room_Management_Form

#-------- Django Generic Import--------#
from django.views.generic.edit import FormView
from django.views.generic import (
    ListView,
    UpdateView,
    DeleteView,
    
)


#--------  Model Import --------#
from .models import Room_Management,User_Room_Management

#-------------------------------- Class Based View's --------------------------------#

#-------- Room Management Form Logic--------#
@method_decorator(staff_member_required, name='dispatch')
class Room_Management_View(LoginRequiredMixin,View):
    def get(self, request):
        form = Room_Management_Form()
        return render(request, 'room_management/room_management_form.html',{'form':form})   

    def post(self, request,*args, **kwargs):
        form = Room_Management_Form(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'room_management/room_management_form.html',{'form':form})

#-------- Room Management List View--------#
@method_decorator(staff_member_required, name='dispatch')
class Room_ManagementListView(ListView):
    model = Room_Management
    context_object_name = 'room_availability'
    template_name = 'room_management/room_availability.html'

    def get_queryset(self):
        return Room_Management.objects.filter().order_by('room_number')

#-------- Room Management Update View--------#
@method_decorator(staff_member_required, name='dispatch')
class RoomUpdateView(UpdateView,FormView):
    model = Room_Management
    template_name = 'room_management/room_availability_form.html'
    
    success_url = reverse_lazy("room-list")
    form_class=Room_Management_Form    
    
#-------- Room Management Delete View--------#
@method_decorator(staff_member_required, name='dispatch')
class RoomEntryDeleteView(DeleteView):
    model = Room_Management
    success_url = reverse_lazy("room-list")
    template_name = 'room_management/room_entry_confirm_delete.html'

#--------User Room Management Detail View--------#

@staff_member_required
def detail_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={
        'room_availability': Room_Management.objects.get(id = id),
        'user_in_room': User_Room_Management.objects.all()

    }
    return render(request,"room_management/room_user_detail.html", context)    


#--------Add User In Room  View--------#

@method_decorator(staff_member_required, name='dispatch')
class Add_User_Room_Management_View(LoginRequiredMixin,View):
    def get(self, request):
        form = User_room_Management_Form()
        return render(request, 'room_management/add_user_in_room.html',{'form':form})   

    def post(self, request,*args, **kwargs):
        form = User_room_Management_Form(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'room_management/add_user_in_room.html',{'form':form})

#--------User Room Management Update View--------#
@method_decorator(staff_member_required, name='dispatch')
class User_RoomUpdateView(UpdateView,FormView):
    model = User_Room_Management
    template_name = 'room_management/add_user_in_room.html'
    success_url = reverse_lazy("room-list")
    form_class=User_room_Management_Form     

#--------Room Delete View--------#         
@method_decorator(staff_member_required, name='dispatch')
class RoomEntryDeleteView(DeleteView):
    model = User_Room_Management
    success_url = reverse_lazy("room-list")
    template_name = 'room_management/user_room_entry_confirm_delete.html'    



#-------- Staff Decorator Logic Function --------#

def staff_member_required(view_func=None, redirect_field_name=REDIRECT_FIELD_NAME,
                          login_url='admin:login'):
    """
    Decorator for views that checks that the user is logged in and is a staff
    member, redirecting to the login page if necessary.
    """
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_staff,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if view_func:
        return actual_decorator(view_func)
    return actual_decorator