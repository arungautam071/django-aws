from django.contrib import admin

#-------- Model Import --------#
from .models import complaint

# Register your models here.

@admin.register(complaint)
class ComplaintModelAdmin(admin.ModelAdmin):
 list_display = ['id', 'user_complain', 'complain_title', 'complain_description', 'complain_date', 'image', 'complain_type']