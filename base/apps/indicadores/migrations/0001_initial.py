# Generated by Django 2.0.2 on 2019-01-14 01:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('evaluaciones', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('actualizado', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=250)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AsignacionIndicadores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('actualizado', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('observaciones_encargado', models.TextField(blank=True, null=True)),
                ('compromiso_del_evaluado', models.TextField(blank=True, null=True)),
                ('debe_mejorar', models.BooleanField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Calificacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('actualizado', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('rango', models.CharField(max_length=150)),
                ('valor', models.PositiveSmallIntegerField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Indicador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('actualizado', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('nombre', models.CharField(max_length=150)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='indicadores.Area')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='asignacionindicadores',
            name='calificacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='calificaciones', to='indicadores.Calificacion'),
        ),
        migrations.AddField(
            model_name='asignacionindicadores',
            name='evaluacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='evaluaciones', to='evaluaciones.Evaluacion'),
        ),
        migrations.AddField(
            model_name='asignacionindicadores',
            name='indicador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='indicadores', to='indicadores.Indicador'),
        ),
    ]
