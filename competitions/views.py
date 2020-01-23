from django.shortcuts import render
from .models import Event, Category, Participant, Entry
#from .forms import ParticipantFormset
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

def addEntry(req, event_id):
    context = {
            'categories' : Category.objects.filter(event_id=event_id)
    }
    if req.method == 'POST':
        participant = Participant()
        participant.first_name = req.POST.get('first_name')
        participant.last_name = req.POST.get('last_name')
        participant.birthday = req.POST.get('birthday')
        print(req.POST.get('category'))
        participant.save()
        entry = Entry()
        entry.participant = participant
        entry.category = Category.objects.get(pk=req.POST.get('category'))
        entry.save()

    return render(req, 'competitions/participant_form.html', context)

