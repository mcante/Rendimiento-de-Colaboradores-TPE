# Generated by Django 2.0.2 on 2019-01-23 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluaciones', '0003_auto_20190119_2313'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evaluacion',
            name='incentivo_mes',
        ),
        migrations.RemoveField(
            model_name='evaluacion',
            name='resultado',
        ),
        migrations.AlterField(
            model_name='version',
            name='descripcion',
            field=models.TextField(max_length=250),
        ),
    ]
