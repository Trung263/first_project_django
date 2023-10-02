import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')
import django
django.setup()

## FAKE POP SCRIPT
import random
from first_app.models import Topic,AccessRecord,Webpage,FormUser
from task3.models import CustomUser
from faker import Faker
fakegen = Faker()
topics = ['Search','Social','Maketplace',' News','Game']

def app_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        top = app_topic()


        faker_url = fakegen.url()
        faker_date = fakegen.date()
        faker_name = fakegen.company()

        #create new webpage entry
        webpg = Webpage.objects.get_or_create(topic=top,url=faker_url,name=faker_name)[0]
        # create acces record
        acc_rec = AccessRecord.objects.get_or_create(name=webpg,date=faker_date)[0]



def populateUser(N=5):
    for entry in range(N):
        
        #faker_name = fakegen.name().split()
        faker_first_name = fakegen.first_name()
        faker_last_name = fakegen.last_name()
        faker_email = fakegen.email()

        # CustomUser.objects.get_or_create(first_name=faker_first_name,last_name=faker_last_name,email=faker_email)[0]

def createUser(fname, femail,ftext):
    fusers = FormUser.objects.get_or_create(name=fname,email=femail,text=ftext)[0]
    return fusers
     

     

# if __name__ ==  '__main__':
#             print("populating script!")
#             populateUser(20)
#             print('populating complate!')


populateUser(20)