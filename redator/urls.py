from django.urls import path, include
from .views import RedatoresList, RedatorDetail, RedatorChange, RedatorUpdate, RedatorDelete

urlpatterns = [
    path('redatores/', RedatoresList.as_view(), name="lista_redatores"),
    path('redator/<int:pk>', RedatorDetail.as_view(), name="redator"),
    path('redator/<int:pk>/change', RedatorChange.as_view(), name="ban_redator"),
    path('redator/<int:pk>/edit', RedatorUpdate.as_view(), name="att_redator"),
    path('redator/<int:pk>/delete', RedatorDelete.as_view(), name="del_redator"),

]