from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_usuarios, name='lista_usuarios'),
    path('adicionar/', views.adicionar_usuario, name='adicionar_usuario'),
    path('editar/<int:id>/', views.editar_usuario, name='editar_usuario'),
    path('excluir/<int:id>/', views.excluir_usuario, name='excluir_usuario'),
]
