from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import RequestContext, loader
from django.utils import timezone


from .models import Doctors, WorkTime, Entries


def index(request):   
    doctors_list = Doctors.objects.order_by('doctor_name')[:]
    work_time_list = WorkTime.objects.order_by('id')[:]
    entries_list = Entries.objects.filter(entry_date__gte=timezone.now())[:]    
    template = loader.get_template('entries/index.html')
    context = RequestContext(request, {
        'doctors_list': doctors_list,
        'work_time_list': work_time_list,
        'entries_list' : entries_list,                         
    })
    return HttpResponse(template.render(context))
