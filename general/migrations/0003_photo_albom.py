# Generated by Django 2.2 on 2020-03-04 20:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0002_auto_20200304_1957'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='albom',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='general.Albom'),
            preserve_default=False,
        ),
    ]