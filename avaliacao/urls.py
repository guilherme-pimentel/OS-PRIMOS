from django.urls import path
from . import views

urlpatterns = [
    path("", views.lista_avaliacao, name="lista_avaliacao"),
    path("adicionar/", views.adicionar_avaliacao, name="adicionar_avaliacao"),
    path("editar/<int:id>/", views.editar_avaliacao, name="editar_avaliacao"),
    path("excluir/<int:id>/", views.excluir_avaliacao, name="excluir_avaliacao"),
    path('detalhe/<int:id>/', views.detalhe_avaliacao, name='detalhe_avaliacao'),
]