# Generated by Django 5.0.3 on 2024-04-12 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('route', '0011_alter_route_options_alter_route_preparation_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='preparation_date',
            field=models.DateField(blank=True, default='2024-04-12', null=True, verbose_name='Fecha de Creacion'),
        ),
        migrations.AlterField(
            model_name='route',
            name='preparation_time',
            field=models.TimeField(blank=True, default='12:32:05', null=True, verbose_name='Hora de Creacion'),
        ),
        migrations.AlterField(
            model_name='routeinstance',
            name='isinstance_date',
            field=models.DateField(blank=True, default='2024-04-12', null=True),
        ),
        migrations.AlterField(
            model_name='routeinstance',
            name='isinstance_time',
            field=models.TimeField(blank=True, default='12:32:05', null=True, verbose_name='Hora de Creacion'),
        ),
    ]
