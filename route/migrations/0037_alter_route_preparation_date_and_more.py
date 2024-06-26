# Generated by Django 5.0.3 on 2024-04-26 23:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('route', '0036_alter_route_preparation_time_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='preparation_date',
            field=models.DateField(blank=True, default='2024-04-26', null=True, verbose_name='Fecha de Creacion'),
        ),
        migrations.AlterField(
            model_name='route',
            name='preparation_time',
            field=models.TimeField(blank=True, default='20:59:43', null=True, verbose_name='Hora de Creacion'),
        ),
        migrations.AlterField(
            model_name='routeinstance',
            name='instance_date',
            field=models.DateField(blank=True, default='2024-04-26', null=True),
        ),
        migrations.AlterField(
            model_name='routeinstance',
            name='instance_time',
            field=models.TimeField(blank=True, default='20:59:43', null=True, verbose_name='Hora de Creacion'),
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nodo', models.ManyToManyField(to='route.nodedestination')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
