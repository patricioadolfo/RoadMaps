# Generated by Django 5.0.3 on 2024-04-12 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('route', '0014_alter_route_preparation_time_alter_route_state_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='preparation_time',
            field=models.TimeField(blank=True, default='15:06:47', null=True, verbose_name='Hora de Creacion'),
        ),
        migrations.AlterField(
            model_name='routeinstance',
            name='isinstance_time',
            field=models.TimeField(blank=True, default='15:06:47', null=True, verbose_name='Hora de Creacion'),
        ),
    ]
