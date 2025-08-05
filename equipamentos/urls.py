from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_equipamentos, name='lista_equipamentos'),
    path('adicionar/', views.adicionar_equipamento, name='adicionar_equipamento'),
    path('editar/<int:id>/', views.editar_equipamento, name='editar_equipamento'),
    path('excluir/<int:equipamento_id>/', views.excluir_equipamento, name='excluir_equipamento'),

]
