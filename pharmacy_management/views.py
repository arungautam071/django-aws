#-------- Django Import --------#
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic import DeleteView,ListView,UpdateView,CreateView
from django.urls import  reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test

#-------- Model Import --------#
from .models import pharmacy_model

#-------- Form Import --------#
from pharmacy_management.forms import pharmacy_status_update_admin_Form

# Create your views here.

#-------- create view --------
class pharmacy_requestCreateView(LoginRequiredMixin, CreateView):
    model = pharmacy_model
    fields = ['request_time', 'prescription','prescription_text']
    template_name = 'pharmacy_management/pharmacy_request_form.html'
    success_url = reverse_lazy("pharamacy_request-list")

    def form_valid(self, form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)     


     
 
#-------- Detail view --------
#------- pharmacy prescription show -------
@staff_member_required
def detail_view_pharmacy(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={
        'pharmacy':pharmacy_model.objects.get(id = id)
    }
    return render(request,"pharmacy_management/detail_pharamacy_request.html", context)  

#-------- Delete view --------
@method_decorator(staff_member_required, name='dispatch')
class pharmacy_requestDeleteView(LoginRequiredMixin, DeleteView):
    model = pharmacy_model
    success_url = reverse_lazy("pharamacy_request-list")
    template_name = 'pharmacy_management/pharamacy_request_confirm_delete.html'


#-------- Update view --------    
@method_decorator(staff_member_required, name='dispatch')
class pharmacy_requestUpdateView(UpdateView,FormView):
    model = pharmacy_model
    template_name = 'pharmacy_management/pharamacy_status_update_form.html'
    
    success_url = reverse_lazy("pharamacy_request-list")       
    form_class=pharmacy_status_update_admin_Form

#-------- List view --------
@method_decorator(staff_member_required, name='dispatch')
class pharamacy_request_ListView(ListView):
    model = pharmacy_model
    context_object_name = 'pharamacy_request'
    template_name = 'pharmacy_management/show_all_pharamacy_request.html'

    def get_queryset(self):
        return pharmacy_model.objects.filter().order_by('-request_time')        
    


#-------- Decorator function --------
def staff_member_required(
    view_func=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url="admin:login"
):
    """
    Decorator for views that checks that the user is logged in and is a staff
    member, redirecting to the login page if necessary.
    """
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_staff,
        login_url=login_url,
        redirect_field_name=redirect_field_name,
    )
    if view_func:
        return actual_decorator(view_func)
    return actual_decorator    