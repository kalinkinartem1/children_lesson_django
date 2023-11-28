from django.shortcuts import render
from .models import Schedule

def index(request):
    schedules = Schedule.objects.all()
    return render(request, 'app/index.html', {'schedules': schedules})
