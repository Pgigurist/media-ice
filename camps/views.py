from django.shortcuts import render
from .models import Camp

# Create your views here.
def camps(req):
    context = {
        'events' : Camp.objects.all().reverse()
    }
    return render(req, 'competitions/list.html', context)
