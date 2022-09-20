#-------- Django Import--------#
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views import View
from django.views.generic import DetailView,UpdateView,DeleteView,CreateView
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404

#-------- Model Import--------#
from .models import Service_Amenities_Request_Model,User_Food_Request,Washing_machine_request

#-------- Form Import-------#
from .forms import Food_Request_Form, Service_Amenities_Request_Form,Washing_machine_request_Form
from django.views.generic.edit import FormView

##-------- Staff Decorator import --------#
# from django.contrib.auth import REDIRECT_FIELD_NAME
# from django.contrib.auth.decorators import user_passes_test
# from django.contrib.admin.views.decorators import staff_member_required
# from django.utils.decorators import method_decorator


# Create your views here.

#-------- Food Request View --------#
class FoodRequest(LoginRequiredMixin,View):


 def get(self, request):
  form = Food_Request_Form()
  return render(request, 'user_request/user_request_form.html', {'form':form})   


 def post(self, request,*args, **kwargs):
  form = Food_Request_Form(request.POST,request.FILES,)
  form.instance.user_request = request.user
  if form.is_valid():
   form.save()
   return render(request, 'user_request/user_request_form.html', {'form':form})

#-------- Service Amenities request View --------#
class Service_Amenities_Request(LoginRequiredMixin,View):


 def get(self, request):
  form = Service_Amenities_Request_Form()
  return render(request, 'user_request/Service_Amenities_Request_Form.html', {'form':form})   


 def post(self, request,*args, **kwargs):
  form = Service_Amenities_Request_Form(request.POST)
  form.instance.user_request = request.user
  if form.is_valid():
   form.save()
   return render(request, 'user_request/Service_Amenities_Request_Form.html', {'form':form})

#-------- Washing Machine request View --------#   

class Washing_machine_Request_View(LoginRequiredMixin,View):
    def get(self, request):
        form = Washing_machine_request_Form()
        return render(request, 'user_request/washing_form.html', {'form':form})   


    def post(self, request,*args, **kwargs):
        form = Washing_machine_request_Form(request.POST,)
        form.instance.user_request = request.user
        if form.is_valid():
            form.save()
        return render(request, 'user_request/washing_form.html', {'form':form})



 

#-------- Service Amenities View To Show All The Request--------#

def show_request(request):
    context = {
        'service_request': Service_Amenities_Request_Model.objects.all()
    }
    return render(request, 'user_request/show_service_amenities_request.html', context)   

#-------- Request View To Show All The Food Request--------#
def show_food_request(request):
    context = {
        'Food_request': User_Food_Request.objects.all()
    }
    return render(request, 'user_request/food_request_show.html', context)  



#-------- Washing View To Show All The Washing Request--------#      

def show_washing_request(request):
    context = {
        'washing_machine': Washing_machine_request.objects.all()
    }
    return render(request, 'user_request/show_washing_request.html', context)  



class WashingDetailView(DetailView):
    model = Washing_machine_request      
    template_name = 'user_request/Washing_machine_request_detail.html'

#--------Washing Delete View --------#

class WashingDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Washing_machine_request
    success_url = '/user/washing_request_show/'
    template_name = 'user_request/washing_confirm_delete.html'

    def test_func(self):
        complaint = self.get_object()
        if self.request.user == complaint.user_request:
            return True
        return False



#--------Washing Update View --------#
class WashingUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView,FormView):
    model = Washing_machine_request
    template_name = 'user_request/washing_form.html'
    
    success_url = '/user/washing_request_show/'
    form_class=Washing_machine_request_Form
    

    def form_valid(self, form):
        form.instance.user_request = self.request.user
        return super().form_valid(form)

    def test_func(self):
        complaint = self.get_object()
        if self.request.user == complaint.user_request:
            return True
        return False



#-------- Staff Decorator Logic Function --------#

# def staff_member_required(view_func=None, redirect_field_name=REDIRECT_FIELD_NAME,
#                           login_url='admin:login'):
#     """
#     Decorator for views that checks that the user is logged in and is a staff
#     member, redirecting to the login page if necessary.
#     """
#     actual_decorator = user_passes_test(
#         lambda u: u.is_active and u.is_staff,
#         login_url=login_url,
#         redirect_field_name=redirect_field_name
#     )
#     if view_func:
#         return actual_decorator(view_func)
#     return actual_decorator