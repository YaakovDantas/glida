from django.urls import path, include
from .views import ArtigoList, ArtigoDetail, ArtigoChange, ArtigoDelete

urlpatterns = [
    path('artigos/', ArtigoList.as_view(), name="lista_artigo"),
    path('artigo/<int:pk>', ArtigoDetail.as_view(), name="artigo"),
    path('artigo/<int:pk>/edit', ArtigoChange.as_view(), name="att_art"),
    path('artigo/<int:pk>/delete', ArtigoDelete.as_view(), name="del_art"),

]