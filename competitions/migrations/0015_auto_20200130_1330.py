# Generated by Django 2.2 on 2020-01-30 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0014_auto_20200128_1036'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='abbreviation',
        ),
        migrations.AlterField(
            model_name='event',
            name='date_start',
            field=models.DateField(verbose_name='День начала'),
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(verbose_name='день окончания'),
        ),
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.CharField(max_length=150, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='event',
            name='place',
            field=models.CharField(blank=True, max_length=200, verbose_name='Место'),
        ),
    ]