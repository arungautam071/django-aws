
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


#-------- Room Management model--------#

class Room_Management(models.Model):
    room_user_main=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    room_number=models.IntegerField(null=True)
    room_type=models.CharField(max_length=50)
    room_status=models.CharField(max_length=50)
    check_in_date=models.DateField(null=True)
    room_for=models.CharField(max_length=50)
    room_floor=models.CharField(max_length=50,blank=True)


#--------User Room Management model--------#

class User_Room_Management(models.Model):
    room_user=models.ForeignKey(Room_Management,on_delete=models.CASCADE,null=True)
    room_user_name=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return str(self.room_user)


    



    
    
        
                        
