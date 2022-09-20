#-------- Django import--------#
from django.urls import  reverse_lazy
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    DeleteView
)
from django.views import View
#-------- Staff Decorator Logic --------#
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator

#-------Model Import--------#
from services_management.models import complaint
from user_management.models import Profile
# from user_management.models import Profile
from room_management.models import User_Room_Management
#-------Registeration Form import--------#
from .forms import UserRegisterForm
from .forms import UserUpdateForm
from .forms import ProfileUpdateForm
from .forms import Contact_form

# Create your views here.
def home(request):
    context = {
        'complaints': complaint.objects.all()
    }
    return render(request, 'user_management/home.html', context)


@method_decorator(staff_member_required, name='dispatch')
class ComplainListView(ListView):
    model = complaint
    template_name = 'user_management/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'complaints'
    ordering = ['-complain_date']
    paginate_by = 5    

# pricing page render
def pricing(request):
    return render(request, 'user_management/price.html')    

#contact From render
# def contact_form(request):
#     return render(request, 'user_management/contact_form.html')     

# index page render

def index(request):
    return render(request, 'user_management/index.html')   


    
#-------- User Registeration Logic --------#

def register(request):
    if request.method == 'POST':
        form= UserRegisterForm(request.POST)
        if form.is_valid():
            
            username=form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            form.save()
            return redirect('Login')
           
    else:
        form = UserRegisterForm()
    return render(request,'user_management/register.html',{'form':form})


#-------- Profile  Logic --------#

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }

    return render(request, 'user_management/profile.html', context)

#--------User Profile List View --------#  
#-------- List view --------

class Profile_ListView(ListView):
    model = Profile
    context_object_name = 'user_profile'
    template_name = 'user_management/profile_list.html'

    def get_queryset(self):
        return Profile.objects.filter().order_by('-date_of_joining')  


#-------- Profile Detail View --------
        


# --------------------experiment -------- #
@staff_member_required 
def User_Profile_DetailView(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={
        'room_availability': User_Room_Management.objects.get(id = id),
        'p_form':ProfileUpdateForm(instance=request.user.profile)

    }
    return render(request,"user_management/user_profile_detail.html", context)  

# --------------------experiment

# class User_Profile_DetailView(DetailView):
#     model = User_Room_Management      
#     template_name = 'user_management/user_profile_detail.html'    

#-------- Complain Class Based View's--------#

class UserComplainListView(ListView):
    model = complaint
    context_object_name = 'complaints'
    paginate_by = 5
    template_name = 'user_management/complaint_list.html'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return complaint.objects.filter(user_complain=user).order_by('-complain_date')    
        

class ComplaintDetailView(DetailView):
    model = complaint      
    template_name = 'user_management/complaint_detail.html'



class ComplaintDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = complaint
    success_url = reverse_lazy("home-page")
    template_name = 'user_management/complaint_confirm_delete.html'

    def test_func(self):
        complaint = self.get_object()
        if self.request.user == complaint.user_complain:
            return True
        return False



#--------Complain Update View --------#
class ComplaintUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = complaint
    template_name = 'user_management/complaint_form.html'
    fields = ['complain_title', 'complain_description','image']
    success_url = reverse_lazy("home-page")

    def form_valid(self, form):
        form.instance.user_complain = self.request.user
        return super().form_valid(form)

    def test_func(self):
        complaint = self.get_object()
        if self.request.user == complaint.user_complain:
            return True
        return False



class Contact_form_detail(View):
    def get(self, request):
        form = Contact_form()
        return render(request, 'user_management/contact_form.html',{'form':form})   

    def post(self, request,*args, **kwargs):
        form = Contact_form(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'user_management/contact_form.html',{'form':form})


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