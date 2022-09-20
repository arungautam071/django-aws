from django import forms

#-------- Model Import --------#
from .models import User_Food_Request,Service_Amenities_Request_Model,Washing_machine_request


FOOD_CHOICES = [
 ('Breakfast', 'Breakfast'),
 ('Lunch', 'Lunch'),
 ('Dinner','Dinner')
]
SERVICE_TYPE = [
 ('Request Service', 'Request Service'),
 ('Amenities', 'Amenities'),
]
WASHING_MACHINE_TYPE = [
 ('MACHINE-1','MACHINE-1'),
 ('MACHINE-2', 'MACHINE-2'),
]
WASHING_MACHINE_STATUS = [
 ('Occupied','Occupied'),
 ('Reserved For Next Turn', 'Reserved For Next Turn'),
]
#-------- Form Logic complain Form--------#

class Food_Request_Form(forms.ModelForm):
    food_type_request = forms.ChoiceField(choices=FOOD_CHOICES, widget=forms.RadioSelect)
    class Meta:
        model=User_Food_Request
        fields=['food_type_request','request_date']
        
        
#-------- Service Amenities Form--------#

class Service_Amenities_Request_Form(forms.ModelForm):
    service_type_request = forms.ChoiceField(choices=SERVICE_TYPE, widget=forms.RadioSelect)
    class Meta:
        model=Service_Amenities_Request_Model
        fields=['service_type_request','service_title']


#-------- Washing Machine Form--------#

class Washing_machine_request_Form(forms.ModelForm):
    machine_number = forms.ChoiceField(choices=WASHING_MACHINE_TYPE, widget=forms.RadioSelect)
    status = forms.ChoiceField(choices=WASHING_MACHINE_STATUS, widget=forms.RadioSelect)
    class Meta:
        model=Washing_machine_request
        fields=['mobile_number','put_in_time','take_out_time','machine_number','status']      