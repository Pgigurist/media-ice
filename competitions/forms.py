from django import forms
from django.forms.models import BaseInlineFormSet

from .models import Participant, Performance, Entry
from django.forms.models import inlineformset_factory

ParticipantFormset = inlineformset_factory(models.Participant, models.Entry, extra=1)

