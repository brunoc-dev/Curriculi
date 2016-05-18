from django.db import models

# Create your models here.


class Script(models.Model):
	nome = models.CharField(max_length = 100)
	comentario = models.TextField(max_length = 100)

	def __str__(self):
		return self.nome


class Linguagem(models.Model):
	lingua = models.CharField(max_length = 100)
	descLingua = models.TextField(max_length = 200)

	def __unicode__(self):
		return self.lingua

class Conhecimento(models.Model):
	linguagens = models.ForeignKey(Linguagem)
	nivelConhecimento = models.CharField (max_length = 50)


class Curso(models.Model):
	nomeDoCurso = models.CharField(max_length = 100)
	duracao = models.CharField(max_length = 100)
	descCurso = models.TextField(max_length = 1024)

	def __unicode__(self):
		return self.nomeDoCurso

class Formacao(models.Model):
	curso = models.ForeignKey(Curso)
	dataConclusao = models.DateField('Data de Conclusao')
	instituicao = models.CharField(max_length = 100)

class Idioma(models.Model):
	nomeIdioma = models.CharField(max_length = 100)
	nivEsc = models.CharField(max_length = 50)
	nivLeitura = models.CharField(max_length = 50)
	nivOral = models.CharField(max_length = 50)

	def __str__(self):
		return self.nomeIdioma

class Experiencia(models.Model):
	empresa = models.CharField(max_length = 100)
	area = models.CharField(max_length = 100)
	tempo = models.CharField(max_length = 50)
	descAtividade = models.TextField(max_length = 200)


class Vaga(models.Model):
	nomeVaga = models.CharField(max_length = 100)
	descVaga = models.TextField(max_length = 100)
	quantidade = models.IntegerField(default = 0)

	def __str__(self):
		return self.nomeVaga


class Candidato(models.Model):
	nomeCanditato = models.CharField(max_length = 100)
	tel1 = models.CharField(max_length = 11)
	tel2 = models.CharField(max_length = 11)
	email = models.EmailField(max_length = 100)
	exp = models.ForeignKey(Experiencia)
	idiomas = models.ForeignKey(Idioma)
	formacao = models.ForeignKey(Formacao)
	conhecimentos = models.ForeignKey(Conhecimento)
	logradouro = models.CharField(max_length = 200)
	numeroLog = models.CharField(max_length = 10)
	bairro = models.CharField(max_length = 200)
	cep = models.IntegerField(default = 0)
	complemento = models.CharField(max_length = 100)
	vagaPret = models.ForeignKey(Vaga)

	def __str__(self):
		return self.nomeCanditato
