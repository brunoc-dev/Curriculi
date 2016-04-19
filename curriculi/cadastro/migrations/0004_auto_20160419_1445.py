# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0003_auto_20160419_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='descCurso',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='experiencia',
            name='descAtividade',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='linguagem',
            name='descLingua',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='vaga',
            name='descVaga',
            field=models.TextField(max_length=100),
        ),
    ]
