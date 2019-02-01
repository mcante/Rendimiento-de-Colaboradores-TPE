# Generated by Django 2.0.2 on 2019-01-14 01:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('faltas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='llamadaatencion',
            name='levantada_por',
        ),
        migrations.AddField(
            model_name='llamadaatencion',
            name='levantada_por',
            field=models.ManyToManyField(related_name='levantada', to=settings.AUTH_USER_MODEL),
        ),
    ]
