from django.db import models
from django.utils.translation import ugettext_lazy as _
from general.models import EventBase

# Create your models here.
class Camp(EventBase):
    """
    name = models.CharField(max_length=150, verbose_name=_("Название"))
    place = models.CharField(max_length=200,  verbose_name=_("Место"), blank=True)
    short_name = models.CharField(max_length=100)
    date_start = models.DateField( verbose_name=_("День начала"))
    date_end = models.DateField()
    description = models.TextField( verbose_name=_("день окончания"))
    """
    class Meta:
        verbose_name = 'Лагерь'
        verbose_name_plural = 'Сборы'
