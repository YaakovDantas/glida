from django.urls import path, include
from .views import GerentesList, GerenteDetail, GerenteCreate, GerenteChange, GerenteUpdate, GerenteDelete


urlpatterns = [
    path('gerentes/', GerentesList.as_view(), name="lista_gerentes"),
    path('gerente/<int:pk>', GerenteDetail.as_view(), name="gerente"),
    path('gerente/create', GerenteCreate.as_view() ,name="create_gerente"),
    path('gerente/<int:pk>/change',GerenteChange.as_view(), name="ban_gerente"),
    path('gerente/<int:pk>/edit',GerenteUpdate.as_view(), name="att_gerente"),
    path('gerente/<int:pk>/delete', GerenteDelete.as_view(), name="del_gerente"),
]