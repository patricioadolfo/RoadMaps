# Generated by Django 5.0.3 on 2024-04-02 11:46

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('route', '0004_alter_route_barcode_alter_route_preparation_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='route',
            name='status',
        ),
        migrations.RemoveField(
            model_name='route',
            name='time',
        ),
        migrations.CreateModel(
            name='RouteInstance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='ID único', primary_key=True, serialize=False)),
                ('status', models.CharField(blank=True, choices=[('p', 'Preparado'), ('c', 'En camino'), ('e', 'Entregado'), ('r', 'Recibido')], default='p', max_length=1, verbose_name='Estado')),
                ('time', models.DateField(blank=True, null=True)),
                ('id_route', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='route.route')),
            ],
            options={
                'ordering': ['time'],
            },
        ),
    ]
