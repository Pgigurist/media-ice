from django.db import models

# Create your models here.
class Camp(models.Model):
    name = models.CharField(max_length=150)
    place = models.CharField(max_length=200, blank=True)
    short_name = models.CharField(max_length=100)
    date_start = models.DateField()
    date_end = models.DateField()
    description = models.TextField()

    class Meta:
        verbose_name = 'Лагерь'
        verbose_name_plural = 'Сборы'
