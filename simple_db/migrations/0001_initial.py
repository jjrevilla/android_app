# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('articulo', models.TextField(max_length=20)),
                ('stack', models.IntegerField()),
                ('costo', models.FloatField(max_length=10)),
            ],
            options={
                'verbose_name_plural': 'Articulos',
            },
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.IntegerField()),
                ('costo', models.FloatField(max_length=10)),
                ('codigo_articulo', models.ForeignKey(to='simple_db.Articulo')),
            ],
            options={
                'verbose_name_plural': 'Pedidos',
            },
        ),
    ]
