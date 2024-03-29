# Generated by Django 2.2 on 2020-01-21 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0002_auto_20200121_1845'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='birthday',
            field=models.DateField(blank=True, default='0001-01-01'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='participant',
            name='club_name',
            field=models.CharField(default='0001-01-01', max_length=110),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='participant',
            name='coach_name',
            field=models.CharField(default='default', max_length=100),
            preserve_default=False,
        ),
    ]
