# Generated by Django 2.2 on 2020-01-16 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('city', models.CharField(max_length=100)),
                ('text', models.TextField(blank=True)),
                ('moderate', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'отзыв',
                'verbose_name_plural': 'отзывы',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('image', models.ImageField(upload_to='media/images/')),
            ],
            options={
                'verbose_name': 'фото',
                'verbose_name_plural': 'фотографии',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('description', models.CharField(blank=True, max_length=500)),
                ('text', models.TextField(blank=True)),
                ('image', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='general.Photo')),
            ],
            options={
                'verbose_name': 'публикация',
                'verbose_name_plural': 'новости',
            },
        ),
    ]
