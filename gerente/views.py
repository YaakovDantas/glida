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


class GerentesList(LoginRequiredMixin,ListView):
    login_url = '/login/' 
    paginate_by = 12
    template_name = 'gerente/gerente_list.html'

    def get_queryset(self):
        gerentes = Gerente.objects.values('pk')
        usuarios = User.objects.filter(gerente__pk__in=gerentes).order_by('pk')
        return usuarios
        # return User.gerente.get_queryset()
        # return User.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super(GerentesList, self).get_context_data(**kwargs)
        return context

class GerenteDetail(LoginRequiredMixin,DetailView):
    login_url = '/login/'
    model = Gerente
    template_name = 'gerente/gerente_detail.html'

   
    def get_context_data(self, **kwargs):
        context = super(GerenteDetail, self).get_context_data(**kwargs)
        return context


class GerenteUpdate(LoginRequiredMixin,UpdateView):
    login_url = '/login/' 
    model = User
    fields = ["username","password","email"]
    # form_class = GerenteForm
    template_name = 'gerente/gerente_form.html'
    success_url = '/dashboard/gerentes/'   



    def get_context_data(self, **kwargs):
        context = super(GerenteUpdate, self).get_context_data(**kwargs)
        return context


class GerenteCreate(LoginRequiredMixin,CreateView):
    model = User
    #form_class = UserForm
    success_url ="/dashboard/gerentes/"
    # success_url ="/login"
    template_name = 'gerente/gerente_form.html'
    fields=['username','email','password']	#
    def form_valid(self,form):
        user = form.save(commit=False)

        user.set_password(user.password)
        user.save()
        r = Gerente()
        r.login_senha=user
        r.save()

        
        return super(GerenteCreate, self).form_valid(form)


class GerenteChange(LoginRequiredMixin,RedirectView):
    permanent = False
    query_string = False
    pattern_name = 'gerente'

    def get_success_url(self):
        return reverse('lista_gerentes')

    def get_redirect_url(self, *args, **kwargs):
        artigo = get_object_or_404(Gerente, pk=kwargs['pk'])
        artigo.toggle_ativo()
        return self.get_success_url()


class GerenteDelete(LoginRequiredMixin,DeleteView):
    login_url = '/login/' 
    model = Gerente
    template_name = 'gerente/gerente_delete.html'
    success_url = '/dashboard/gerentes/'
