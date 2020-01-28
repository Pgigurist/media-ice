from django.db import models
from django.conf import settings
# Create your models here.


class Participant(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=80)
    birthday = models.DateField()
    club_name = models.CharField(max_length=110)
    coach_name = models.CharField(max_length=100)

    def full_name(self):
        return self.first_name+' '+self.last_name

    class Meta:
        verbose_name = 'Участник'
        verbose_name_plural = 'Участники'

    def __str__(self):
        return self.full_name()

   
class Event(models.Model):
    # primary fields
    name = models.CharField(max_length=150)
    place = models.CharField(max_length=200, blank=True)
    short_name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=10)
    date_start = models.DateField()
    date_end = models.DateField()
    description = models.TextField()
    # custom fields
    annoncment = models.FileField(blank=True)
    event_protocol = models.FileField(blank=True)
    published = models.BooleanField(default=False)
    youtube_link = models.URLField(blank=True)

    class Meta:
        verbose_name = 'соревнование'
        verbose_name_plural = 'соревнования'
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=150)
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    event = models.ForeignKey(Event, related_name='event_id', on_delete=models.CASCADE)
    price = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

class Segment(models.Model):
    # choices dictionary
    GENDER_CHOICES = (
        ('M', 'Мужчины/Юноши/Мальчики'),
        ('F', 'Женщины/Девушки/Девочки'),
        ('C', 'Пары'),
    )

    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    category = models.ForeignKey(Category, related_name='category_id', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Сегмент'
        verbose_name_plural = 'Сегменты'

    def __str__(self):
        return self.name+' '+self.category.name

class Entry(models.Model):
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    payment = models.BooleanField(default=False)
    music = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
    def __str__(self):
        name = self.participant.last_name
        return name+' '+self.category.name

def content_file_name(instance, filename):
    return settings.MUSIC_DIR.join+instance.user.id+filename

class Performance(models.Model):
    segment = models.ForeignKey(Segment, on_delete=models.CASCADE)
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE)
    start_number = models.IntegerField(default=0)
    points = models.FloatField(default=0.0)


    music = models.FileField(upload_to=settings.MUSIC_DIR, blank=True)
    

    class Meta:
        verbose_name = 'Прокат'
        verbose_name_plural = 'Прокаты'

