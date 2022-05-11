from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Video, Event
from .forms import VideoForm
import os
from datetime import datetime
from django.views import generic
from django.utils.safestring import mark_safe
from .utils import Calendar
from .pro import process

def showvideo(request):

    # lastvideo= Video.objects.last()

    # videofile= lastvideo.videofile


    form= VideoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/success')

    
    context= {
              'form': form
              }
    
      
    return render(request, 'upload.html', context)

def success(request):
    lastvideo= Video.objects.last()
    videofile= lastvideo.videofile
    local_path = videofile.path
    print(local_path)
    return render(request, "success.html", {
        "videofile": videofile,
        "path": local_path
    })

def add(request,path):
    process(path)
    return HttpResponseRedirect('/calendar')


class CalendarView(generic.ListView):
    model = Event
    template_name = 'calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # use today's date for the calendar
        d = get_date(self.request.GET.get('day', None))

        # Instantiate our calendar class with today's year and date
        cal = Calendar(d.year, d.month)

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        return context

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()