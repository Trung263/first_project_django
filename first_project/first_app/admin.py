from django.contrib import admin
from first_app.models import AccessRecord, Topic, Webpage,FormUser

# Register your models here.
class CustomFormUser(admin.ModelAdmin):
    list_display = ['name','email','text']
    search_fields = ['name','email','text']
    list_editable = ['text']

class CustomWebpage(admin.ModelAdmin):
    fields = ['url','name']
    

admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(Webpage,CustomWebpage)
admin.site.register(FormUser,CustomFormUser)


    