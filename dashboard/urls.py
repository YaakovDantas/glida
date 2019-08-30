from django.urls import path, include
from .views import DashboardView, DashboardLoginView, DashboardLogoutView, ComentarioDelete, SugestaoCreate

urlpatterns = [
    path('', DashboardView.as_view(), name="dashboard"),
    path('login/', DashboardLoginView.as_view(), name="dashboard_login"),
    path('logout/', DashboardLogoutView.as_view(), name="dashboard_logout"),
    path('comentario/<int:pk>/delete', ComentarioDelete.as_view(), name="del_coment"),
    path('sugestao', SugestaoCreate.as_view(), name="create_sugestao"),

    path("",include('artigo.urls')),
    path('',include('redator.urls')),
    path('',include('gerente.urls')),
    path('',include('tema.urls')),
    path('',include('contato.urls')),

]
