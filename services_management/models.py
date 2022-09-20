#-------- Django Import--------#
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

#--------Pillow Import--------#
from PIL import Image


#--------Logic For Complaint Model--------#

class complaint(models.Model):
    user_complain=models.ForeignKey(User,on_delete=models.CASCADE) 
    complain_title=models.CharField(max_length=100)
    complain_description=models.TextField()
    complain_date=models.DateTimeField(default=timezone.now)
    image=models.ImageField(default='default_food.jpg',upload_to='complain_pic')
    complain_type=models.CharField(max_length=50)

    def __str__(self):
        return f'{self.user_complain.username} complain'

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)

    #     img=Image.open(self.image.path)
    #     if img.height > 300 or img.width > 300:
    #         output_size=(300,300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)
    
    
    