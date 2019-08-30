from django.urls import path, include
from .views import ContatosList, ContatoDetail, ContatoChange, ContatoDelete


urlpatterns = [
    path('contatos/', ContatosList.as_view(), name="lista_contatos"),
    path('contato/<int:pk>', ContatoDetail.as_view(), name="contato"),
    
    path('contato/<int:pk>/change',ContatoChange.as_view(), name="alter_contato"),
    path('contato/<int:pk>/delete', ContatoDelete.as_view(), name="del_contato"),
]