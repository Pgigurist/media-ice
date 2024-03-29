# Generated by Django 2.2 on 2020-01-28 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0013_auto_20200123_1819'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='performance',
            options={'verbose_name': 'Прокат', 'verbose_name_plural': 'Прокаты'},
        ),
        migrations.AlterField(
            model_name='performance',
            name='music',
            field=models.FileField(blank=True, upload_to='./competitions/'),
        ),
        migrations.AlterField(
            model_name='performance',
            name='points',
            field=models.FloatField(default=0.0),
        ),
    ]
