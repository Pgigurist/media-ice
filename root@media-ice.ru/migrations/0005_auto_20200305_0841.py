# Generated by Django 2.2 on 2020-03-05 08:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camps', '0004_coachlist'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coachlist',
            options={'verbose_name': 'Список тренеров', 'verbose_name_plural': 'Списки тренеров'},
        ),
        migrations.RemoveField(
            model_name='coachlist',
            name='camp',
        ),
        migrations.RemoveField(
            model_name='coachlist',
            name='coach',
        ),
    ]