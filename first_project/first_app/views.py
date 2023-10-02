from django.shortcuts import render
from .forms import FormName 
from first_app.models import AccessRecord,FormUser
import populate_first_app

# Create your views here.

def index(request):
    webpae_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpae_list}
    return render(request,'index.html',context=date_dict)

def form_name_view(request):
    form = FormName()
    if request.method == 'POST':
        form = FormName(request.POST)

        if form.is_valid():
            print('Validation success!')  
            print('Name: '+form.cleaned_data['name']) 
            print('Email: '+form.cleaned_data['email']) 
            print('Text: '+form.cleaned_data['text']) 
            fname = form.cleaned_data['name']
            femail = form.cleaned_data['email']
            ftext = form.cleaned_data['text']
            populate_first_app.createUser(fname,femail,ftext)
    return render(request,'basic_app/form.html',{'form':form})

def basic_index(request):
    return render(request,'basic_app/index.html')

def list_fUser(request):
    user_list = FormUser.objects.all()
    stt_list = {'access':user_list}
    return render(request,'basic_app/index.html', context=stt_list)

