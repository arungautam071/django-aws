#-------- Django Form Import --------#
from django import forms

#-------- Model Import--------#
# from .models import Room_Management
from .models import User_Room_Management
from .models import Room_Management

#--------Radio Button Input--------#

Room_Type = [
 ('Single', 'Single'),
 ('Double', 'Double'),
 ('Triple','Triple'),
 ('Four-sharing','Four-sharing')
]
Room_Status=[
    ('Available','Available'),
    ('Not-Available','Not-Available')
]
Room_For=[
    ('Boy','Boy'),
    ('Girl','Girl'),
    ('Couple','Couple')
]

Room_Floor=[
    ('First-floor','First-floor'),
    ('Second-floor','Second-floor'),
    ('Third-floor','Third-floor'),
    ('Forth-floor','Forth-floor'),

]


#-------- Form Logic Room Management Form--------#

class Room_Management_Form(forms.ModelForm):
    room_type = forms.ChoiceField(choices=Room_Type, widget=forms.RadioSelect)
    room_status = forms.ChoiceField(choices=Room_Status, widget=forms.RadioSelect)
    room_for = forms.ChoiceField(choices=Room_For, widget=forms.RadioSelect)
    room_floor = forms.ChoiceField(choices=Room_Floor, widget=forms.RadioSelect)
    check_in_date = forms.DateField(required=False)
    class Meta:
        model=Room_Management
        fields=['room_number','room_type','room_floor','room_status','room_for','check_in_date']

class User_room_Management_Form(forms.ModelForm):
    # room_type = forms.ChoiceField(choices=Room_Type, widget=forms.RadioSelect)
    # room_status = forms.ChoiceField(choices=Room_Status, widget=forms.RadioSelect)
    # room_for = forms.ChoiceField(choices=Room_For, widget=forms.RadioSelect)
    # check_in_date = forms.DateField(required=False)
    class Meta:
        model=User_Room_Management
        fields=['room_user','room_user_name']      
        # widgets={
        #         'room_user': forms.TextInput(attrs={'for':'exampleSelect1','class':'form-select','id':'exampleSelect1'}),
        #         'room_user_name': forms.TextInput(attrs={'class':'form-select','id':'exampleSelect1t'})
        #         }