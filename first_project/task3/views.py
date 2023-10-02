from django.shortcuts import render
from task3.models import CustomUser

# Create your views here.

def user_list(request):
    user_list = CustomUser.objects.all()
    stt_list = {'access':user_list}
    return render(request,'list.html', context=stt_list)
