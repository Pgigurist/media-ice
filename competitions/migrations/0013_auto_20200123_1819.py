# Generated by Django 2.2 on 2020-01-23 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0012_auto_20200123_1743'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='description',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Performance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_number', models.IntegerField(default=0)),
                ('points', models.FloatField(blank=True)),
                ('music', models.FileField(blank=True, upload_to='')),
                ('entry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='competitions.Entry')),
                ('segment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='competitions.Segment')),
            ],
        ),
    ]