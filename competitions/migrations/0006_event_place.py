# Generated by Django 2.2 on 2020-01-23 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0005_event_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='place',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]