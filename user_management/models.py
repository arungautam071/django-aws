#-------- Django import--------#
from email import message
from email.mime import image
from email.policy import default
from faulthandler import disable
from pyexpat import model
from typing_extensions import Required
from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone

#--------User Profile Logic--------#
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    mobile_number=PhoneNumberField(blank=True)
    date_of_joining=models.DateTimeField(default=timezone.now)
    residental_address=models.CharField(max_length=150,blank=True)
    office_college_address=models.CharField(max_length=300,blank=True)
    emergency_contact_relationship=models.CharField(max_length=30,blank=True)
    emergency_contact_mobile_number=PhoneNumberField(blank=True)
    monthly_rent=models.IntegerField(null=True,blank=True)
    security_amount=models.IntegerField(null=True,blank=True)
    id_proof_document_name=models.CharField(max_length=30,blank=True)
    id_proof_document=image=models.ImageField(blank=True,upload_to='documents_pics')
    image=models.ImageField(default='default.jpg', upload_to='profile_pics')
    user_room_number=models.IntegerField(blank=True,null=True,)
    last_pay_date=models.DateTimeField(null=True, blank=True)
    current_month_pay_status=models.CharField(max_length=50,blank=True)
    

    def __str__(self):
        return f'{self.user.username} Profile'

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)

    #     img = Image.open(self.image.path)

    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)    


class Contact_Form_Model(models.Model):
    name=models.CharField(max_length=70)
    contact_number=models.CharField(max_length=50)
    subject=models.CharField(max_length=50,blank=True)
    message=models.CharField(max_length=50,blank=True)