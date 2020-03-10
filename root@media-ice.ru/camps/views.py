from django.shortcuts import render
from .models import Camp, Group, Photo, CoachList

# Create your views here.
def camps(req):
    context = {
        'events' : Camp.objects.all().reverse()
    }
    return render(req, 'camps/events_list.html', context)

def camp(req, camp_id):

    event = Camp.objects.get(pk=camp_id)
    groups = Group.objects.filter(camp=event)
    photos = Photo.objects.filter(albom=event.albom)
    coaches = CoachList.objects.filter(camp=event) 

    context = {
        'event' : event,
        'groups' : groups,
        'photos' : photos,
        'coaches' : coaches,
            }

    return render(req, 'camps/camp.html', context)
