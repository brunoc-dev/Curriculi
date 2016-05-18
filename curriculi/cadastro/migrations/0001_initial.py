# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidato',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nomeCanditato', models.CharField(max_length=100)),
                ('tel1', models.CharField(max_length=11)),
                ('tel2', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=100)),
                ('logradouro', models.CharField(max_length=200)),
                ('numeroLog', models.CharField(max_length=10)),
                ('bairro', models.CharField(max_length=200)),
                ('cep', models.IntegerField(default=0)),
                ('complemento', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Conhecimentos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nivelConhecimento', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Cursos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nomeDoCurso', models.CharField(max_length=100)),
                ('duracao', models.CharField(max_length=100)),
                ('descCurso', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Experiencia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('empresa', models.CharField(max_length=100)),
                ('area', models.CharField(max_length=100)),
                ('tempo', models.CharField(max_length=50)),
                ('descAtividade', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Formacao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dataConclusao', models.DateField(verbose_name=b'Data de Conclusao')),
                ('instituicao', models.CharField(max_length=100)),
                ('curso', models.ForeignKey(to='cadastro.Cursos')),
            ],
        ),
        migrations.CreateModel(
            name='Idiomas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nomeIdioma', models.CharField(max_length=100)),
                ('nivEsc', models.CharField(max_length=50)),
                ('nivLeitura', models.CharField(max_length=50)),
                ('nivOral', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Linguagens',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lingua', models.CharField(max_length=100)),
                ('descLingua', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('login', models.CharField(max_length=100)),
                ('senha', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Vagas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nomeVaga', models.CharField(max_length=100)),
                ('descVaga', models.CharField(max_length=100)),
                ('quantidade', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='conhecimentos',
            name='linguagens',
            field=models.ForeignKey(to='cadastro.Linguagens'),
        ),
        migrations.AddField(
            model_name='candidato',
            name='conhecimentos',
            field=models.ForeignKey(to='cadastro.Conhecimentos'),
        ),
        migrations.AddField(
            model_name='candidato',
            name='exp',
            field=models.ForeignKey(to='cadastro.Experiencia'),
        ),
        migrations.AddField(
            model_name='candidato',
            name='formacao',
            field=models.ForeignKey(to='cadastro.Formacao'),
        ),
        migrations.AddField(
            model_name='candidato',
            name='idiomas',
            field=models.ForeignKey(to='cadastro.Idiomas'),
        ),
        migrations.AddField(
            model_name='candidato',
            name='usuario',
            field=models.ForeignKey(to='cadastro.Usuario'),
        ),
        migrations.AddField(
            model_name='candidato',
            name='vagaPret',
            field=models.ForeignKey(to='cadastro.Vagas'),
        ),
    ]
