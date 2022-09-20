from django.contrib import admin
from pharmacy_management.models import pharmacy_model

# Register your models here.


@admin.register(pharmacy_model)
class pharmacy_modelModelAdmin(admin.ModelAdmin):
 list_display = ['id', 'user_name', 'request_time', 'status', 'prescription', 'billing_amount']