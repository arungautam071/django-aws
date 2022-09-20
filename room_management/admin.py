from django.contrib import admin
from .models import User_Room_Management,Room_Management

# Register your models here.

#-------- Room Management admin page register--------#
@admin.register(Room_Management)
class Room_ManagementModelAdmin(admin.ModelAdmin):
    list_display = ['id','room_number','room_user_main','room_type','room_floor','room_for','room_status','check_in_date']

@admin.register(User_Room_Management)
class User_Room_ManagementModelAdmin(admin.ModelAdmin):
    list_display = ['id','room_user','room_user_name']

