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

class ArtigoDetail(LoginRequiredMixin,  DetailView):
    login_url = '/login' 
    model = Artigo
    template_name = 'artigo/artigo_detail.html'

   
    def get_context_data(self, **kwargs):
        context = super(ArtigoDetail, self).get_context_data(**kwargs)
        return context

class ArtigoList( LoginRequiredMixin, ListView):
    login_url = '/login' 
    paginate_by = 12
    template_name = 'artigo/artigo_list.html'

    def get_queryset(self):
        return Artigo.objects.all().order_by('pk')
    
    def get_context_data(self, **kwargs):
        context = super(ArtigoList, self).get_context_data(**kwargs)
        return context
    
class ArtigoDelete(LoginRequiredMixin,  DeleteView):
    login_url = '/login' 
    model = Artigo
    template_name = 'artigo/artigo_delete.html'
    success_url = '/dashboard/artigos/'


class ArtigoChange( LoginRequiredMixin, RedirectView):
    login_url = '/login' 
    permanent = False
    query_string = False
    pattern_name = 'artigo'

    def get_success_url(self):
        return reverse('lista_artigo')

    def get_redirect_url(self, *args, **kwargs):
        artigo = get_object_or_404(Artigo, pk=kwargs['pk'])
        artigo.toggle_ativo()
        return self.get_success_url()

    # login_url = '/login/' 
    # model = Artigo
    # fields = ['ativo']
    # template_name = 'dashboard/artigo/artigo_form.html'
    # success_url = '/dashboard/artigos/'   
    
    # def get_context_data(self, **kwargs):
    #     context = super(ArtigoUpdate, self).get_context_data(**kwargs)
    #     return context
