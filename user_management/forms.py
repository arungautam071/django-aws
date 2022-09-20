
#-------- Django Import--------#
from pyexpat import model
from statistics import mode
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

#-------- Model And Form Import--------#

from .models import Profile,Contact_Form_Model

#-------- Form Logic For registration--------#





#-------- Register Form--------#
class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model =User
        fields=['username','email','password1','password2']
        

#-------- Update Form --------#
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

#--------Profile Update Form--------#
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['current_month_pay_status','last_pay_date','mobile_number','residental_address','office_college_address','emergency_contact_relationship','emergency_contact_mobile_number','monthly_rent','security_amount','id_proof_document_name','id_proof_document','image','user_room_number']
        labels={'mobile_number':'Mobile Number','residental_address':'Residential Address'
        ,'office_college_address':'Office Or College Address','emergency_contact_relationship':'Emergency Contact Relationship'
        ,'emergency_contact_mobile_number':'Emergency Contact Number'
        ,'monthly_rent':'Monthly Rent','security_amount':'Security Amount','id_proof_document_name':'ID Proof Document Name','id_proof_document':'ID Proof Document'
        ,'image':'Profile Image','user_room_number':'User Room Number','current_month_pay_status':'Current Pay Status','last_pay_date':'Last Pay Date'}
        widgets={
                'mobile_number': forms.TextInput(attrs={'class':'form-control', 'type':'tel', 'id':'inputDefault','placeholder':'+91**********'}),
                'emergency_contact_mobile_number': forms.TextInput(attrs={'class':'form-control', 'type':'tel', 'id':'inputDefault','placeholder':'+91**********'}),
                'office_college_address': forms.TextInput(attrs={'class':'form-control', 'type':'text', 'id':'inputDefault','placeholder':'Your Office / College Address Here'}),
                'residental_address': forms.TextInput(attrs={'class':'form-control', 'type':'text', 'id':'inputDefault','placeholder':'Your Address Here'}),
                'emergency_contact_relationship': forms.TextInput(attrs={'class':'form-control', 'type':'text', 'id':'inputDefault','placeholder':'Parents / Brother'}),
                'id_proof_document_name': forms.TextInput(attrs={'class':'form-control', 'type':'text', 'id':'inputDefault','placeholder':'Aadhar / Pan-Card'}),
                'id_proof_document': forms.FileInput(attrs={'class':'form-control', 'type':'file', 'id':'formFile'}),
                'image': forms.FileInput(attrs={'class':'form-control', 'type':'file', 'id':'formFile'}),
                'monthly_rent': forms.NumberInput(attrs={'class':'form-control', 'id':'number','disabled':'True'}),
                'security_amount': forms.NumberInput(attrs={'class':'form-control', 'id':'number','disabled':'True'}),
                'current_month_pay_status': forms.TextInput(attrs={'class':'form-control', 'id':'text','disabled':'True'}),
                'last_pay_date': forms.DateInput(attrs={'class':'form-control', 'id':'date','disabled':'True'}),
                }



#-------- Contact Form --------
     
class Contact_form(forms.ModelForm):
    class Meta:
        model = Contact_Form_Model 
        fields = ['name','contact_number','subject','message']
        labels={'name':'Your Name','contact_number':'Your Contact Number','subject':'Subject','message':'Message'}
        widgets={
                'name': forms.TextInput(attrs={'class':'form-control', 'type':'text', 'id':'inputDefault','placeholder':'Name...'}),
                'contact_number': forms.TextInput(attrs={'class':'form-control', 'type':'text', 'id':'inputDefault','placeholder':'+91**********'}),
                'subject': forms.TextInput(attrs={'class':'form-control', 'type':'text', 'id':'inputDefault','placeholder':'subject...'}),
                'message': forms.TextInput(attrs={'class':'form-control', 'type':'text', 'id':'inputDefault','placeholder':'Message...'}),
                }