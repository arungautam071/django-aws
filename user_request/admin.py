from django.contrib import admin

#-------- Model Import --------#
from .models import User_Food_Request,Service_Amenities_Request_Model,Washing_machine_request

# Register your models here.

@admin.register(User_Food_Request)
class User_Food_RequestModelAdmin(admin.ModelAdmin):
    list_display = ['user_request', 'request_date', 'food_type_request']


@admin.register(Service_Amenities_Request_Model)
class Service_Amenities_Request_ModelModelAdmin(admin.ModelAdmin):
    list_display = ['user_request', 'service_type_request', 'service_title','service_status','request_date']


@admin.register(Washing_machine_request)
class Washing_machine_requestModelAdmin(admin.ModelAdmin):
    list_display = ['user_request', 'mobile_number', 'machine_number','status','put_in_time','take_out_time']