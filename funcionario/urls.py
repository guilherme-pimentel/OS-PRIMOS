from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_funcionario, name='lista_funcionarios'),
    path('adicionar/', views.adicionar_funcionario, name='adicionar_funcionario'),
    path('editar/<int:id>/', views.editar_funcionario, name='editar_funcionario'),
    path('excluir/<int:id>/', views.excluir_funcionario, name='excluir_funcionario'),
    path('detalhe/<int:id>/', views.detalhe_funcionario, name='detalhe_funcionario')
]