from django.shortcuts import render
from .models import Event, Category, Participant, Entry

# Create your views here.

def list(req):
    context = {
        'events' : Event.objects.all().reverse()
    }

    """
    if competition == null:
        context = {
            'events' : Event.objects.all().reverse()
        }
        return render(req, 'competitions/list.html', context)
    else:
        context = {
            'events' : Event.objects.all().reverse()
        }
    """
    return render(req, 'competitions/list.html', context)
def event(req, event_id):
    print('get event req')
    print(event_id)
    pass

