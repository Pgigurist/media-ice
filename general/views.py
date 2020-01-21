from django.shortcuts import render
from .models import Post, Photo, Feedback
from .forms import FeedbackForm

# Create your views here.

def index(req):
    context = {
        'photos' : Photo.objects.all().reverse()[:3],
        'posts' : ''
    }
    return render(req, 'general/index.html', context)

def gallery(req):
    context = {
        'photos' : Photo.objects.all().reverse()
    }
    return render(req, 'general/gallery.html', context)

def feedback(req):
    posts = Feedback.objects.all().order_by('pub_date').reverse()
    if req.method == 'POST':
        form = FeedbackForm(req.POST)
        if form.is_valid():
            feedback = form.save()
            return render(req, 'general/index.html')
        else:
            form = FeedbackForm()
            context = {
                'posts' : posts,
                'feedback_form' : form,
            }
        return render(req, 'general/feedback.html', context)
    return render(req, 'general/feedback.html', {'posts':posts})

def gallery(req):
    context = {
        'photos'    :   Photo.objects.all().reverse()
    }
    return render(req, 'general/gallery.html', context)

