from django.db import models
from django.utils.translation import ugettext_lazy as _
from general.models import EventBase, Photo, Albom
from django.utils.timezone import now

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
    albom = models.ForeignKey(Albom, related_name='current_albom_id', on_delete=models.CASCADE, blank=True) 
    class Meta:
        verbose_name = 'Лагерь'
        verbose_name_plural = 'Сборы'
    def __str__(self):
        return self.name

class Group(models.Model):
    camp = models.ForeignKey(Camp, related_name='camp_id', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, verbose_name='название')
    description = models.TextField(verbose_name='описание')

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def __str__(self):
        return self.title+' '+self.camp.name

class Coach(models.Model):
    class Meta:
        verbose_name = 'Тренер'
        verbose_name_plural = 'Тренеры'
    name = models.CharField(max_length=100, verbose_name='ФИО')
    description = models.TextField(verbose_name='Описание')
    photo = models.ForeignKey(Photo, related_name='photo_id', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class CoachList(models.Model):
    class Meta:
        verbose_name = 'Список тренеров'
        verbose_name_plural = 'Списки тренеров'
    camp = models.ForeignKey(Camp, on_delete=models.CASCADE)
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE)
    def __str__(self):
        return self.coach.name

