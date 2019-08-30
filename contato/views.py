from django.shortcuts import render
from django.shortcuts import render,redirect, reverse, get_object_or_404
from django.http import HttpResponse
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.base import View, RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin
from home.models import Gerente, Redator, Artigo, Comentario, Tema, Contato
from django.contrib.auth.models import User

# Create your views here.

class ContatosList(ListView):
    login_url = '/login/' 
    paginate_by = 12
    template_name = 'contato/contato_list.html'

    def get_queryset(self):
        return Contato.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super(ContatosList, self).get_context_data(**kwargs)
        return context

class ContatoDetail(DeleteView):
    login_url = '/login/'
    model = Contato
    template_name = 'contato/contato_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super(ContatoDetail, self).get_context_data(**kwargs)
        return context

class ContatoChange(RedirectView):
    permanent = False
    query_string = False
    pattern_name = 'contato'

    def get_success_url(self):
        return reverse('lista_contatos')

    def get_redirect_url(self, *args, **kwargs):
        artigo = get_object_or_404(Contato, pk=kwargs['pk'])
        artigo.toggle_ativo()
        return self.get_success_url()

class ContatoDelete(DeleteView):
    login_url = '/login/' 
    model = Contato
    template_name = 'contato/contato_delete.html'
    success_url = '/dashboard/contatos/'



class ContatoCreate(CreateView):
	login_url = '/login/'
	model = Contato
	template_name = 'home/contact.html'
	fields = ['nome', 'email', 'assunto', 'mensagem']
	success_url = '/'

	def get_context_data(self, **kwargs):
		context = super(ContatoCreate, self).get_context_data(**kwargs)
		context['temas'] = Tema.objects.all()
		context['user_logado'] =  self.request.user if self.request.user.is_active  else False
		return context














   
   

    



    