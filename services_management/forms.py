#-------- Django import--------#

from django import forms

#-------- model import--------#

from .models import complaint

#--------Radio Button Input--------#
COMPLAIN_CHOICES = [
 ('Food', 'Food'),
 ('Cleaning', 'Cleaning')
]

#-------- Form Logic complain Form--------#

class complainForm(forms.ModelForm):
    complain_type = forms.ChoiceField(choices=COMPLAIN_CHOICES, widget=forms.RadioSelect)
    class Meta:
        model=complaint
        fields=['complain_type','complain_title','complain_description','complain_date','image']
        labels = {'complain_type':'Complain Type', 'complain_title': 'Title', 'complain_description':'Complain Description', 'complain_date':'Date','image':'Image'}
        widgets={
                'image': forms.FileInput(attrs={'class':'form-control', 'type':'file', 'id':'formFile'}),
                }



