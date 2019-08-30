from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic.edit import FormView, UpdateView, CreateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.base import View, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Redator, Artigo, Comentario, Tema, Visualizacao, Acesso,Contato
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import (authenticate, get_user_model, login, logout)
from .forms import ComentarioForm, BuscaForm

# Create your views here.

class HomeListView(ListView):
	login_url = '/login/' 
	paginate_by = 5
	template_name = "home/index.html"

	def get_queryset(self):
		if 'busca' in self.request.GET:
			query = self.request.GET['busca']
			artigos = Artigo.objects.filter(ativo=True, titulo__contains = query )
		elif 'pk' in self.kwargs:
			tema_pk = self.kwargs['pk']
			artigos = Artigo.objects.filter(ativo=True, tema=tema_pk)
		else:
			artigos = Artigo.objects.filter(ativo=True)
		return artigos

	def get_context_data(self, **kwargs):
		context = super(HomeListView, self).get_context_data(**kwargs)
		# context['temas'] = Tema.objects.all()
		# context['user_logado'] =  self.request.user if self.request.user.is_active  else False
		
		return context




class RedatorCreate(CreateView):
	# model = Redator
	model = User
	#form_class = UserForm
	success_url ="/"
	# success_url ="/login"
	template_name = 'home/registro_form.html'
	fields=['username','email','password']	#
	def form_valid(self,form):
		user = form.save(commit=False)

			
		# if User.objects.filter(email=user.email).exclude(username=user.username).exists():
		# 	form.add_error('email','Este email já existe, tente outro.')
		# 	return self.form_invalid(form)
		
		user.set_password(user.password)
		user.save()
		r = Redator()
		r.login_senha=user
		r.save()

		
		return super(RedatorCreate, self).form_valid(form)

class LoginView(View):
	def get(self, request):
		context = {}
		if('next' in request.GET):
			next_url = request.GET['next']
			context['next_url'] = next_url
		return render(request, "home/login.html", context)

	def post(self, request):
		if (len(request.POST) != 0):
			username = request.POST['username']
			password = request.POST['password']
			next_url = request.POST['next_url'] if 'next_url' in request.POST  else None
			
			# user =  Redator.objects.filter(login_senha__username=username)[0]
			user =  User.objects.filter(username=username)[0]
			#user = authenticate( )
			senha_valida = check_password(password, user.password)
			
			
			if user is not None and senha_valida:
				login(request, user)
				
				ir_para = next_url if next_url != None else '/'
				return redirect(ir_para)
				#return  HttpResponse('logado')
			else:
				#print('user n existe')
				return render(request, "home/login.html",{'form':"form"})
				#print ('USUARIO',request.user.username)

		else:
			
			return render(request, "home/login.html")
			#return render(request, "login.html")

class LogoutView(View):
	def get(self, request):
		logout(request)	
		return redirect('login')

class ArtigoCreate(CreateView):
	login_url = '/login/'
	model = Artigo
	template_name = 'home/create_artigo.html'
	fields = ['titulo', 'tema', 'texto', ]
	success_url = '/'

	def form_valid(self, form):
		artigo = form.save(commit=False)
		artigo.redator = self.request.user.usuario
		return super(ArtigoCreate, self).form_valid(form)

	def get_context_data(self, **kwargs):
		context = super(ArtigoCreate, self).get_context_data(**kwargs)
		context['temas'] = Tema.objects.all()
		context['user_logado'] =  self.request.user if self.request.user.is_active  else False
		return context

class ArtigoDetail( DetailView):
	login_url = '/login/'
	model = Artigo
	template_name = 'home/post.html'

	def get(self,request,pk,*args,**kwargs):
		artigo = get_object_or_404(Artigo, pk=pk)
		Visualizacao.objects.create(artigo=artigo)
		self.object = self.get_object()
		context = self.get_context_data(object=self.object)
		return self.render_to_response(context) 

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['form'] = ComentarioForm
		context['temas'] = Tema.objects.all()
		context['user_logado'] =  self.request.user if self.request.user.is_active  else False
		return context

class ComentarioCreate(CreateView):
	login_url = '/login/'
	model = Comentario
	# form_class = ComentarioForm
	template_name = 'home/artigo/comentario_form.html'
	fields = ['texto', ]
	# success_url = '/artigo/1'
	def get_success_url(self,**kwargs):
		artigo = str(self.kwargs['pk'])
		return "/artigo/"+artigo

	def form_valid(self, form):
		comentario = form.save(commit=False)
		
		comentario.leitor = self.request.user.usuario
		artigo = get_object_or_404(Artigo, pk=self.kwargs['pk'])
		comentario.artigo = artigo
		comentario.save()
		return super(ComentarioCreate, self).form_valid(form)


class SobreView(View):
	

	def get(self, request, *args,  **kwargs):
		context = {}
		context['temas'] = Tema.objects.all()
		context['user_logado'] =  self.request.user if self.request.user.is_active  else False
		
		return render(request, "home/about.html",context)

class ConfiguracaoView(View):
	

	def get(self, request, *args,  **kwargs):
		context = {}
		context['temas'] = Tema.objects.all()
		context['user_logado'] =  self.request.user if self.request.user.is_active  else False
		
		return render(request, "home/config_conta.html",context)

class RedatorUpdate(UpdateView):
	model = Redator
	fields = ['nome_completo','data_criacao','facebook','twitter','github','instagram','logo','pais','estado','cidade','descricao','telefone']
	template_name = "home/redator_form.html"
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['temas'] = Tema.objects.all()
		context['user_logado'] =  self.request.user if self.request.user.is_active  else False
		return context

class ArtigoConfigList(ListView):
	login_url = '/login/' 
	paginate_by = 5
	template_name = "home/user-artigos_list.html"

	def get_queryset(self):
		artigos = Artigo.objects.filter(redator=self.request.user.usuario.pk)
		return artigos

	def get_context_data(self, **kwargs):
		context = super(ArtigoConfigList, self).get_context_data(**kwargs)
		# context['temas'] = Tema.objects.all()
		# context['user_logado'] =  self.request.user if self.request.user.is_active  else False
		
		return context

class ArtigoConfigUpdate(UpdateView):
	login_url = '/login/'
	model = Artigo
	template_name = 'home/create_artigo.html'
	fields = ['titulo', 'tema', 'texto', ]
	success_url = '/'

class ArtigoConfigDetail(DetailView):
	template_name = "home/fake_post_artigo_detail.html"
	login_url = '/login/'
	model = Artigo