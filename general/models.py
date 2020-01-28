from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class EventBase(models.Model):
    #abstract model
    class Meta:
        abstract = True
    name = models.CharField(max_length=150, verbose_name=_("Название"))
    place = models.CharField(max_length=200,  verbose_name=_("Место"), blank=True)
    short_name = models.CharField(max_length=100)
    date_start = models.DateField( verbose_name=_("День начала"))
    date_end = models.DateField()
    description = models.TextField( verbose_name=_("день окончания"))


class Photo(models.Model):
    title = models.CharField(max_length=300)
    image = models.ImageField(upload_to='media/images/')
    
    class Meta:
        verbose_name = 'фото'
        verbose_name_plural = 'фотографии'

    def __str__(self):
        return self.title


class Post(models.Model):
    name = models.CharField(max_length=300)
    pub_date = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=500, blank=True)
    text = models.TextField(blank=True)
    image = models.ForeignKey(Photo, on_delete=models.CASCADE, blank=True, default=None)
    
    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'новости'


    def __str__(self):
        return self.name

class Feedback(models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    city = models.CharField(max_length=100)
    text = models.TextField(blank=True)
    moderate = models.BooleanField(default=False)


    class Meta:
        verbose_name = 'отзыв'
        verbose_name_plural = 'отзывы'

    def __str__(self):
        string = self.name
        if self.moderate:
            string += ' (опубликовано)'
        else:
            string += ' (новое)'
        return string


