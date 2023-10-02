from django.contrib import admin
from task3.models import CustomUser   

# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['First_Name','Last_Name','Email']

admin.site.register(CustomUser)