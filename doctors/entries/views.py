from django.shortcuts import render

from django.utils import timezone
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

def save(request):
    if request.method == 'POST':         
        entry = Entries(
            create_date = timezone.now(), 
            entry_time = WorkTime.objects.get(id=request.POST['entry_time']), 
            entry_date = request.POST['entry_date'],
            doctor_name = Doctors.objects.get(id=request.POST['doctor_name']),
            client_name = request.POST['client_name'],
        )
        entry.save()
        return HttpResponse('запись сохранена...')
    else:
        return HttpResponse('запись не сохранена...')    

    

    
        
            
      
