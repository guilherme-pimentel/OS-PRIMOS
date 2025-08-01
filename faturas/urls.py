from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_faturas, name='lista_faturas'),
    path('adicionar/', views.adicionar_fatura, name='adicionar_fatura'),
    path('editar/<int:id>/', views.editar_fatura, name='editar_fatura'),
    path('excluir/<int:id>/', views.excluir_fatura, name='excluir_fatura'),
]
