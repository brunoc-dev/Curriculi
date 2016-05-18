# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0004_auto_20160419_1445'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scrip',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=100)),
                ('comentario', models.TextField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='curso',
            name='descCurso',
            field=models.TextField(max_length=1024),
        ),
    ]
