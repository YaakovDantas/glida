from django.shortcuts import render,redirect, reverse, get_object_or_404
from django.http import HttpResponse
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.base import View, RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin
from home.models import Gerente, Redator, Artigo, Comentario, Tema
from django.contrib.auth.models import User
# Create your views here.

class RedatoresList(LoginRequiredMixin,ListView):
    login_url = '/login/' 
    paginate_by = 12
    template_name = 'redator/redator_list.html'

    def get_queryset(self):
        return Redator.objects.all().order_by('pk')
    
    def get_context_data(self, **kwargs):
        context = super(RedatoresList, self).get_context_data(**kwargs)
        return context

class RedatorDetail(LoginRequiredMixin,DetailView):
    login_url = '/login/'
    model = Redator
    template_name = 'redator/redator_detail.html'

   
    def get_context_data(self, **kwargs):
        context = super(RedatorDetail, self).get_context_data(**kwargs)
        return context


class RedatorUpdate(LoginRequiredMixin,UpdateView):
    login_url = '/login/' 
    model = Redator
    fields = ["nome_completo","data_criacao","facebook","twitter","github","instagram","logo","pais","estado","cidade","descricao","telefone"]
    template_name = 'redator/redator_form.html'
    success_url = '/dashboard/redatores/'   
    
    def get_context_data(self, **kwargs):
        context = super(RedatorUpdate, self).get_context_data(**kwargs)
        return context

class RedatorChange(LoginRequiredMixin,RedirectView):
    permanent = False
    query_string = False
    pattern_name = 'redator'

    def get_success_url(self):
        return reverse('lista_redatores')

    def get_redirect_url(self, *args, **kwargs):
        artigo = get_object_or_404(Redator, pk=kwargs['pk'])
        artigo.toggle_ativo()
        return self.get_success_url()

class RedatorDelete(LoginRequiredMixin,DeleteView):
    login_url = '/login/' 
    model = Redator
    template_name = 'redator/redator_delete.html'
    success_url = '/dashboard/redatores/'
