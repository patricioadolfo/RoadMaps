# Generated by Django 5.0.3 on 2024-07-18 00:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('route', '0046_alter_perfil_user_alter_route_preparation_time_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='route',
            name='preparation_time',
            field=models.TimeField(blank=True, default='21:09:20', null=True, verbose_name='Hora de Creacion'),
        ),
        migrations.AlterField(
            model_name='routeinstance',
            name='instance_time',
            field=models.TimeField(blank=True, default='21:09:20', null=True, verbose_name='Hora de Creacion'),
        ),
    ]
