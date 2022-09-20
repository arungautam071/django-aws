#-------- Django Import--------#
from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


#-------- Model And Form Import--------#

from .forms import complainForm


#--------Django Complain Register Form-------#

class ComplainRegister(LoginRequiredMixin,View):

    def get(self, request):
        form = complainForm()
        return render(request, 'services_management/complaint_form.html', {'form':form})   


    def post(self, request,*args, **kwargs):
        form = complainForm(request.POST,request.FILES,)
        form.instance.user_complain = request.user
        if form.is_valid():
            form.save()
        return render(request, 'services_management/complaint_form.html', {'form':form})
  

