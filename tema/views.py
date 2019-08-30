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


class TemasList(ListView):
    login_url = '/login/' 
    paginate_by = 12
    template_name = 'tema/tema_list.html'

    def get_queryset(self):
        return Tema.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super(TemasList, self).get_context_data(**kwargs)
        return context


class TemaDetail(DetailView):
    login_url = '/login/'
    model = Tema
    template_name = 'tema/tema_detail.html'

   
    def get_context_data(self, **kwargs):
        context = super(TemaDetail, self).get_context_data(**kwargs)
        return context


class TemaCreate(CreateView):
    model = Tema
    #form_class = UserForm
    success_url ="/dashboard/temas/"
    # success_url ="/login"
    template_name = 'tema/tema_form.html'
    fields=['nome']	#
       

class TemaUpdate(UpdateView):
    model = Tema
    #form_class = UserForm
    success_url ="/dashboard/temas/"
    # success_url ="/login"
    template_name = 'tema/tema_form.html'
    fields=['nome']	#


class TemaDelete(DeleteView):
    login_url = '/login/' 
    model = Tema
    template_name = 'tema/tema_delete.html'
    success_url = '/dashboard/temas/'
