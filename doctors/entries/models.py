
from django.db import models


#from __future__ import unicode_literals

# Create your models here.

class Doctors(models.Model):    
    create_date = models.DateTimeField('date published')    
    doctor_name = models.CharField(max_length=200)
    def __str__(self):              
        return self.doctor_name

class WorkTime(models.Model):
    time = models.CharField(max_length=200)
    def __str__(self):       
        return self.time      

class Entries(models.Model):    
    create_date = models.DateTimeField('date published')
    entry_time = models.ForeignKey('WorkTime')
    entry_date = models.DateField('entry date')
    doctor_name = models.ForeignKey('Doctors')
    client_name = models.CharField(max_length=200)
    def __str__(self): 
        return str(self.entry_time) + ', ' + str(self.entry_date.strftime('%d.%m.%Y')) + ', ' + str(self.doctor_name) + ', ' + str(self.client_name)
        


