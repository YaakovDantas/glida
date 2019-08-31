from django.shortcuts import render,redirect, reverse, get_object_or_404
from django.http import HttpResponse
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.base import View, RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin
from home.models import Gerente, Redator, Artigo, Comentario, Tema, Acesso, Visualizacao,Contato,Sugestao
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import (authenticate, get_user_model, login, logout)
from django.db.models import Avg, Count, Min, Sum
from .forms import GerenteForm
import datetime, json
# Create your views here.


MONTHS =  {1:'Jan',  2:'Fev',  3:'Mar',  4:'Abr',   5:'Mai',   6:'Jun',
           7:'Jul', 8:'Ago', 9:'Set', 10:'Out', 11:'Nov', 12:'Dez'}

class DashboardView(LoginRequiredMixin,View):

	def get(self, request, *args,  **kwargs):
		

		context = self.get_my_context()
		context = self.get_grafico_temas(context)
		context = self.get_grafico_viss_por_mess(context)
		context = self.get_artigos_chart(context)
		context = self.get_artigos_top(context)
		
		
		return render(request, "dashboard/index.html",context)
	
	def get_my_context(self):
		context = {}
		dia_atual = datetime.date.today()
		mes_atual = dia_atual.month

		viss = Acesso.objects.filter(data=dia_atual).aggregate(Count('data'))
		mensal = Acesso.objects.filter(data__month__exact=mes_atual).aggregate(Count('data'))
		artigo_mais_lido_dia = Visualizacao.objects.filter(data=dia_atual).values('artigo__titulo').annotate(Count('artigo')).order_by('-artigo__count')[0] if  len(Visualizacao.objects.filter(data=dia_atual).values('artigo__titulo').annotate(Count('artigo')).order_by('-artigo__count')) > 0 else { 'artigo__titulo':'Nenhum', 'artigo__count':0 }
		artigo_mais_lido_mes = Visualizacao.objects.filter(data__month__exact=mes_atual).values('artigo__titulo').annotate(Count('artigo')).order_by('-artigo__count')[0] if len(Visualizacao.objects.filter(data__month__exact=mes_atual).values('artigo__titulo').annotate(Count('artigo')).order_by('-artigo__count')) > 0 else  { 'artigo__titulo':'Nenhum', 'artigo__count':0 }
		artigos_total = Artigo.objects.all().count()
		comentarios_total = Comentario.objects.all().count()
		redatores_total = Redator.objects.all().count()
		mensagens_total = Contato.objects.all().count()

		context['dia_viss'] = viss
		context['mensal_viss'] = mensal
		context['artigo_mais_lido_dia'] = artigo_mais_lido_dia
		context['artigo_mais_lido_mes'] = artigo_mais_lido_mes
		context['artigos_total'] = artigos_total
		context['comentarios_total'] = comentarios_total
		context['redatores_total'] = redatores_total
		context['mensagens_total'] = mensagens_total

		return context
	
	def get_grafico_temas(self, context):
		temas_viss = Visualizacao.objects.values('artigo__tema__nome').annotate(Count('artigo'))
		dict_temas = {}
		for item in temas_viss:
			dict_temas[item['artigo__tema__nome']] = item['artigo__count']

		context['temas_viss'] = json.dumps(dict_temas)
		return context
	
	def get_grafico_viss_por_mess(self, context):
		temas_viss =  Acesso.objects.values('data__month').annotate(total=Count('pk'))
		dict_area = {}
		for item in temas_viss:
			mes = MONTHS[ item['data__month']]
			
			dict_area[mes] = item['total']

		context['viss_por_mes'] = json.dumps(dict_area)
		return context
	
	def get_artigos_chart(self,context):
		artigos_pub = Artigo.objects.filter(ativo=True).count()
		artigos_esp = Artigo.objects.filter(ativo=False).count()
		dict_artigo = {
			'Aceitos': artigos_pub,
			'Espera': artigos_esp,
		}
		context['artigos_estado'] = json.dumps(dict_artigo)
		return context
	
	def get_artigos_top(self,context):
		artigos_top = Artigo.objects.filter(ativo=True).values('titulo','redator__login_senha__username').annotate(total_com=Count('comentario', distinct=True)).annotate(total_vis=Count('visualizacao',distinct=True)).order_by('-total_vis','-total_com')
		context['artigos_top'] = artigos_top
		return context

class DashboardLoginView(View):
	def get(self, request):
		context = {}
		if('next' in request.GET):
			next_url = request.GET['next']
			context['next_url'] = next_url
		return render(request, "dashboard/login.html", context)

	def post(self, request):
		if (len(request.POST) != 0):
			username = request.POST['username']
			password = request.POST['password']
			next_url = request.POST['next_url'] if 'next_url' in request.POST  else None
			
			user =  Gerente.objects.filter(login_senha__username=username).exists()
			#user = authenticate( )
			
			if user:
				user =  Gerente.objects.filter(login_senha__username=username)[0]
				user = user.login_senha
				senha_valida = check_password(password, user.password)
				
			
			
				if user is not None and senha_valida:
					login(request, user)
					
					ir_para = next_url if next_url != None else '/dashboard'
					return redirect(ir_para)
					#return  HttpResponse('logado')
				else:
					#print('user n existe')
					return render(request, "dashboard/login.html",{'form':"form"})
					#print ('USUARIO',request.user.username)
			
			return render(request, "dashboard/login.html",{'form':"form"}	)
		else:
			
			return render(request, "dashboard/login.html")

class DashboardLogoutView(View):
	def get(self, request):
		logout(request)	
		return redirect('/dashboard/login') 



class ComentarioDelete( LoginRequiredMixin,DeleteView):
    login_url = '/login/' 
    model = Comentario
    template_name = 'dashboard/comentario/comentario_delete.html'
    success_url = '/dashboard/artigos/'



class SugestaoCreate(LoginRequiredMixin, CreateView):
    model = Sugestao
    fields = ['nome','email','assunto','mensagem']
    template_name = 'dashboard/sugestao_form.html'
    success_url = '/dashboard/'
