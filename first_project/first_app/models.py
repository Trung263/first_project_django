from django.db import models

# Create your models here.
class Topic(models.Model):
    top_name = models.CharField(max_length=264,unique=True)

    def __str__(self):
        return self.top_name

class Webpage(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=264)
    url = models.URLField()

    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage,on_delete=models.CASCADE,)
    date = models.DateField()
   
    def __str__(self):
         return self.date.__str__()
    
class FormUser(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    text = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name


