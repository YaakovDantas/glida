from django.urls import path, include
from .views import HomeListView, RedatorCreate, LoginView, LogoutView, SobreView
from .views import ArtigoCreate, ArtigoDetail, ComentarioCreate, ConfiguracaoView, RedatorUpdate, ArtigoConfigList, ArtigoConfigUpdate, ArtigoConfigDetail
from contato.views import ContatoCreate

urlpatterns = [
    path('', HomeListView.as_view(), name="home"),
    path('<int:pk>', HomeListView.as_view(), name="home_tema"),
    path('registro', RedatorCreate.as_view(), name="registro"),
    path('login', LoginView.as_view(), name="login"),
    path('logout', LogoutView.as_view(), name='logout_brejo'),
    path('artigo/create', ArtigoCreate.as_view(), name="art_create"),
    path('artigo/<int:pk>', ArtigoDetail.as_view(), name="home_art_det"),
    path('comentario/<int:pk>', ComentarioCreate.as_view(), name="com"),
    path('sobre/', SobreView.as_view(), name="sobre"),
    path('contato/create', ContatoCreate.as_view() ,name="create_contato"),
    path('config/', ConfiguracaoView.as_view() ,name="config"),


    path('usuario/<int:pk>/update', RedatorUpdate.as_view() ,name="update_redator"),
    path('usuario/artigos/', ArtigoConfigList.as_view() ,name="lista_artigos_user"),
    path('usuario/artigos/<int:pk>/update', ArtigoConfigUpdate.as_view() ,name="update_artigos_user"),
    path('usuario/artigos/<int:pk>', ArtigoConfigDetail.as_view() ,name="detail_artigos_user"),
    

]
