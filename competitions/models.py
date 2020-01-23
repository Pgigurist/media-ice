from django.db import models
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
    name = models.CharField(max_length=150)
    place = models.CharField(max_length=200, blank=True)
    short_name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=10)
    date_start = models.DateField()
    date_end = models.DateField()
    published = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'соревнование'
        verbose_name_plural = 'соревнования'
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=150)
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    price = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

class Segment(models.Model):
    name = models.CharField(max_length=50)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('C', 'Couple'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Сегмент'
        verbose_name_plural = 'Сегменты'

    def __str__(self):
        return self.name+' '+self.category.name

class Entry(models.Model):
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'


