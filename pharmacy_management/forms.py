#-------- Model Import --------#
from pharmacy_management.models import pharmacy_model

#-------- django Form Import --------#
from django import forms


status_report = [
 ('partially accepted','partially accepted'),
 ('accepted', 'accepted'),
]


#-------- Pharmacy Request Register Form --------#

class pharmacy_model_Form(forms.ModelForm):
    class Meta:
        model=pharmacy_model
        fields=['request_time','prescription','prescription_text']  
        labels={'prescription':'Prescription Image','prescription_text':'Write Your Prescription Here'}
        widgets={
            'prescription': forms.FileInput(attrs={'class':'form-control', 'type':'file', 'id':'formFile'}),
            'prescription_text': forms.TextInput(attrs={'class':'form-control', 'type':'text', 'id':'inputDefault','placeholder':'medicine name....'}),   
                }   

#-------- Pharmacy Request Status Update Form --------#
class pharmacy_status_update_admin_Form(forms.ModelForm):
    status = forms.ChoiceField(choices=status_report, widget=forms.RadioSelect)
    class Meta:
        model=pharmacy_model
        fields=['status']  
        





