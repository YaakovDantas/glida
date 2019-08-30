from django.db import models
from django.contrib.auth.models import User
import datetime


# Create your models here.

class Gerente(models.Model):
	login_senha = models.OneToOneField(User, related_name="gerente",on_delete=models.PROTECT)
	ativo = models.BooleanField(default=True) 
	status = models.CharField(max_length=2, default=0)
	
	
	@property
	def email(self):
		return self.login_senha.email
	
	@property
	def nome(self):
		return self.login_senha.username

	@property
	def password(self):
		return self.login_senha.password
	
	@property
	def usuario(self):
		return self

	def __str__(self):
		return self.login_senha.username

	def toggle_ativo(self):
		self.ativo = not self.ativo
		self.save()


class Redator(models.Model):
	login_senha = models.OneToOneField(User, related_name="usuario",on_delete=models.PROTECT)
	nome_completo = models.CharField(max_length=255, null=True, verbose_name = "Nome completo") 
	data_criacao = models.DateField(("Date"), default=datetime.date.today)
	facebook = models.CharField(max_length=255, null=True, verbose_name = "Link do Facebook")
	twitter = models.CharField(max_length=255, null=True, verbose_name = "Link do Twitter")
	github = models.CharField(max_length=255, null=True, verbose_name = "Link do GitHub")
	instagram = models.CharField(max_length=255, null=True, verbose_name = "Link do Instagram")
	logo = models.FileField(upload_to='fotos', blank=False, null=True, default='fotos/anonymous.jpg', verbose_name = "Foto Perfil")
	pais = models.CharField(max_length=5, default="BR", null=True,  verbose_name = "País, sigla (BR,EUA,CH) ") 
	estado = models.CharField(max_length=4, blank=False, null=False, verbose_name = "Estado") 
	cidade = models.CharField(max_length=80, blank=False, null=False, verbose_name = "Cidade") 
	descricao = models.TextField(max_length=255, null=True, verbose_name = "Descrição")
	telefone = models.CharField(max_length=50, blank=False, null=False, verbose_name = "Telefone (XX)XXXX-XXXX") 
	ativo = models.BooleanField(default=True) 
	status = models.CharField(max_length=2, default=1)

	@property
	def email(self):
		return self.login_senha.email
	
	@property
	def nome(self):
		return self.login_senha.username
	
	@property
	def gerente(self):
		return False

	def all_artigos(self):
		return Artigo.objects.filter(redator=self).count()
	
	def aceitos_artigos(self):
		return Artigo.objects.filter(redator=self, ativo=True).count()
	
	def negados_artigos(self):
		return Artigo.objects.filter(redator=self, ativo=False).count()

	def toggle_ativo(self):
		self.ativo = not self.ativo
		self.save()

	def __str__(self):
		return self.login_senha.username

class Tema(models.Model):
	nome = models.CharField(max_length=80, null=True, verbose_name = "Tema") 
	ativo =  models.BooleanField(default=True) 

	def __str__(self):
		return self.nome


class Artigo(models.Model):
	redator = models.ForeignKey(Redator,on_delete=models.PROTECT)
	tema = models.ForeignKey(Tema,on_delete=models.PROTECT ) 
	titulo = models.CharField(max_length=255, null=True, verbose_name = "Título") 
	texto = models.TextField(blank=False, null=False, verbose_name = "Matéria") 
	ativo = models.BooleanField(default=False) 
	status = models.CharField(max_length=2, default=1)
	data_criacao = models.DateField(("Date"), default=datetime.date.today)


	def __str__(self):
		return self.titulo
	
	def toggle_ativo(self):
		self.ativo = not self.ativo
		self.save()


class Comentario(models.Model):
	artigo = models.ForeignKey(Artigo,on_delete=models.CASCADE)
	leitor = models.ForeignKey(Redator,on_delete=models.PROTECT)
	texto = models.TextField(blank=False, null=False, verbose_name = "Comentario") 
	ativo = models.BooleanField(default=True) 
	status = models.CharField(max_length=2, default=1)
	data_criacao = models.DateField(("Date"), default=datetime.date.today)

	def __str__(self):
		return self.texto


class Acesso(models.Model):
	data = models.DateField(("Date"), default=datetime.date.today)


class Visualizacao(models.Model):
	# gerente = models.ForeignKey(Gerente, on_delete=models.CASCADE, null=True , related_name="gerente")
	# redator = models.ForeignKey(Redator, on_delete=models.CASCADE, null=True , related_name="gerente")
	artigo = models.ForeignKey(Artigo, on_delete=models.CASCADE, null=True,default=5 )
	data = models.DateField(("Date"), default=datetime.date.today)

	@property
	def nome(self):
		if self.artigo:
			nome = self.artigo.titulo
		else:
			nome = 'Nada'
		return nome

	def __str__(self):
		return self.nome

	#Visualizacao.objects.values('artigo__titulo').annotate(Count('artigo'))
	#Visualizacao.objects.values('artigo__tema__nome').annotate(Count('artigo'))
	#Acesso.objects.filter(data__day__exact=23).values('data').annotate(Count('data__day'))

class Contato(models.Model):
	nome = models.CharField(max_length=255, null=False, verbose_name = "Nome") 
	email = models.CharField(max_length=255, null=False, verbose_name = "Email") 
	assunto = models.CharField(max_length=255, null=False, verbose_name = "Assunto") 
	mensagem = models.TextField(null=False, verbose_name = "Mensagem") 
	lido =  models.BooleanField(default=False) 
	data = models.DateField(("Date"), default=datetime.date.today)
	
	def __str__(self):
		return self.assunto
	
	def toggle_ativo(self):
		self.lido = not self.lido
		self.save()


class Sugestao(models.Model):
	IDEIA = 'ideia'
	DUVIDA = 'duvida'
	PROBLEMA = 'problema'
	BUG = 'bug'
	OUTRO = 'outro'
	TIPOS_ASSUNTO = [
		(IDEIA, 'Ideia'),
		(DUVIDA, 'Dúvida'),
		(PROBLEMA, 'Problema'),
		(BUG, 'Bug'),
		(OUTRO, 'Outro'),

	]

	nome = models.CharField(max_length=180, null=False, verbose_name = "Informe seu nome") 
	email = models.CharField(max_length=150, null=False, verbose_name = "Email") 
	assunto = models.CharField(max_length=80, choices=TIPOS_ASSUNTO, default=OUTRO , null=False, verbose_name = "Escolha um assunto") 
	mensagem = models.TextField(max_length=255, null=False, verbose_name = "Mensagem")
	visto = models.BooleanField(default=False) 

	def __str__(self):
		return self.assunto