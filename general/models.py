from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.

 
class Albom(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("Название альбома"))
    class Meta:
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'
    def __str__(self):
        return self.name
  

class Photo(models.Model):
    title = models.CharField(max_length=300, verbose_name=_("Подпись"))
    image = models.ImageField(upload_to='media/images/', verbose_name=_("Изображение"))
    albom = models.ForeignKey(Albom, on_delete=models.CASCADE, blank=True)

    class Meta:
        verbose_name = 'фото'
        verbose_name_plural = 'фотографии'

    def __str__(self):
        return self.title

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


class AbstractPost(models.Model):
 
    POST_TYPE = (
        ('N', 'Новости'),
        ('E', 'Соревнования'),
        ('C', 'Сборы')
    )

   #abstract model for Post/Feedback/News objects
    class Meta:
        abstract = True

    name = models.CharField(max_length=300, verbose_name=_("Название"))
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name=_("Дата публикации"))
    text = models.TextField(blank=True, verbose_name=_("Текст"))
    news_type = models.CharField(max_length=1, verbose_name=_("Тип новости"), choices=POST_TYPE, blank=True)



class Post(AbstractPost):
    """
    name = models.CharField(max_length=300)
    pub_date = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=500, blank=True)
    text = models.TextField(blank=True)
    image = models.ForeignKey(Photo, on_delete=models.CASCADE, blank=True, default=None)
    """
    image = models.ForeignKey(Photo, on_delete=models.CASCADE, blank=True, default=None, verbose_name=_("Изображение"))
    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'новости'


    def __str__(self):
        return self.name

class Feedback(AbstractPost):
    """
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    city = models.CharField(max_length=100)
    text = models.TextField(blank=True)
    """
    moderate = models.BooleanField(default=False, verbose_name=_("Опубликовано"))
    city = models.CharField(max_length=100, verbose_name=_("Город"))


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


