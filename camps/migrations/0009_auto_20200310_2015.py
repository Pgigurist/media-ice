# Generated by Django 2.2 on 2020-03-10 20:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camps', '0008_auto_20200307_1021'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemincluster',
            name='chedule_cluster',
        ),
        migrations.RemoveField(
            model_name='itemincluster',
            name='claster_item',
        ),
        migrations.RemoveField(
            model_name='shedule',
            name='camp',
        ),
        migrations.RemoveField(
            model_name='shedule',
            name='group',
        ),
        migrations.RemoveField(
            model_name='shedulecluster',
            name='shedule',
        ),
        migrations.DeleteModel(
            name='ClusterItem',
        ),
        migrations.DeleteModel(
            name='ItemInCluster',
        ),
        migrations.DeleteModel(
            name='Shedule',
        ),
        migrations.DeleteModel(
            name='SheduleCluster',
        ),
    ]