# Generated by Django 5.0.3 on 2024-03-29 00:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('route', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='routeinstance',
            name='route',
        ),
        migrations.AddField(
            model_name='route',
            name='state',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='route.routeinstance'),
        ),
    ]
