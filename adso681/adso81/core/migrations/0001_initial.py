# Generated by Django 5.0.2 on 2024-03-02 19:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_register', models.DateField(verbose_name='Fecha de registro')),
                ('quantity', models.SmallIntegerField(verbose_name='Cantidad')),
                ('description', models.CharField(max_length=100, verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'Inventario',
                'verbose_name_plural': 'Inventarios',
                'db_table': 'Inventario',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Novedades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Fecha')),
                ('tipe_novedad', models.CharField(max_length=45, verbose_name='Tipo Novedad')),
            ],
            options={
                'verbose_name': 'Novedad',
                'verbose_name_plural': 'Novedades',
                'db_table': 'Novedades',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_donation', models.DateField(verbose_name='Fecha de donacón')),
                ('quantity', models.SmallIntegerField(verbose_name='Cantidad')),
                ('tipe_donation', models.CharField(max_length=15, verbose_name='Tipo de donación')),
                ('inventory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.inventory', verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'Donacion',
                'verbose_name_plural': 'Donaciones',
                'db_table': 'Donaciones',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Inscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_id', models.BigIntegerField(verbose_name='Numero de documento')),
                ('name', models.CharField(max_length=40, verbose_name='Nombre')),
                ('last_name', models.CharField(max_length=40, verbose_name='Apellido')),
                ('nationality', models.CharField(max_length=25, verbose_name='Nacionalidad')),
                ('date_born', models.DateField(verbose_name='Fecha de nacimiento')),
                ('Novedades', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.novedades', verbose_name='Tipo de novedad')),
            ],
            options={
                'verbose_name': 'Inscripcion',
                'verbose_name_plural': 'Inscripciones',
                'db_table': 'Inscripciones',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Incapacidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_inability', models.DateField(verbose_name='Fecha Incapacidad')),
                ('tipe_inability', models.CharField(max_length=46, verbose_name='Tipo Incapacidad')),
                ('no_contact', models.IntegerField(verbose_name='Numero Contacto')),
                ('Novedades', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.novedades', verbose_name='Tipo de novedad')),
            ],
            options={
                'verbose_name': 'Incapacidad',
                'verbose_name_plural': 'Incapacidades',
                'db_table': 'Incapacidad',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_teacher', models.CharField(max_length=45, verbose_name='Nombre instructor')),
                ('date_activity', models.DateField(verbose_name='Fecha Actividad')),
                ('name_activity', models.CharField(max_length=45, verbose_name='Nombre de actividad')),
                ('Novedades', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.novedades', verbose_name='Tipo de novedad')),
            ],
            options={
                'verbose_name': 'Actividad',
                'verbose_name_plural': 'Actividades',
                'db_table': 'Actividad',
                'ordering': ['id'],
            },
        ),
    ]
