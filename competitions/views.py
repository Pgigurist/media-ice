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
    
    event = Event.objects.get(pk=event_id)
    categories = Category.objects.filter(event=event)
    #event.objects.select_related().all()

    context = {
        'event' : event,
        'categories' : categories,
    }
    
    return render(req, 'competitions/event.html', context)

def category(req, category_id):

    category = Category.objects.get(pk=category_id) 
    context = {
        'category' : category,
        'participants' : Entry.objects.filter(category=category)
    }

    return render(req, 'competitions/category.html', context)
