# Generated by Django 2.0.2 on 2019-01-23 17:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('faltas', '0004_auto_20190114_0932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='llamadaatencion',
            name='empleado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='faltas_empleados', to=settings.AUTH_USER_MODEL),
        ),
    ]