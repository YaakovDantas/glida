from django.urls import path, include
from .views import TemasList, TemaDetail, TemaCreate, TemaUpdate, TemaDelete


urlpatterns = [
    path('temas/', TemasList.as_view(), name="lista_temas"),
    path('tema/<int:pk>',TemaDetail.as_view(), name="tema"),
    path('tema/create', TemaCreate.as_view() ,name="create_tema"),
    path('tema/<int:pk>/edit',TemaUpdate.as_view(), name="att_tema"),
    path('tema/<int:pk>/delete',TemaDelete.as_view(), name="del_tema"),
]