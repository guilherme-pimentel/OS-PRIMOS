from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_leituras, name='lista_leituras'),
    path('adicionar/', views.adicionar_leitura, name='adicionar_leitura'),
    path('editar/<int:id>/', views.editar_leitura, name='editar_leitura'),
    path('excluir/<int:id>/', views.excluir_leitura, name='excluir_leitura'),
]
