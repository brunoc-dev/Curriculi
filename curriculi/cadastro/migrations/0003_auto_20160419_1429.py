# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0002_auto_20160419_1421'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conhecimento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nivelConhecimento', models.CharField(max_length=50)),
            ],
        ),
        migrations.RenameModel(
            old_name='Cursos',
            new_name='Curso',
        ),
        migrations.RenameModel(
            old_name='Idiomas',
            new_name='Idioma',
        ),
        migrations.RenameModel(
            old_name='Linguagens',
            new_name='Linguagem',
        ),
        migrations.RenameModel(
            old_name='Vagas',
            new_name='Vaga',
        ),
        migrations.RemoveField(
            model_name='conhecimentos',
            name='linguagens',
        ),
        migrations.AlterField(
            model_name='candidato',
            name='conhecimentos',
            field=models.ForeignKey(to='cadastro.Conhecimento'),
        ),
        migrations.DeleteModel(
            name='Conhecimentos',
        ),
        migrations.AddField(
            model_name='conhecimento',
            name='linguagens',
            field=models.ForeignKey(to='cadastro.Linguagem'),
        ),
    ]
