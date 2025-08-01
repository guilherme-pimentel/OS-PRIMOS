from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_medidores, name='lista_medidores'),
    path('adicionar/', views.adicionar_medidor, name='adicionar_medidor'),
    path('editar/<int:id>/', views.editar_medidor, name='editar_medidor'),
    path('excluir/<int:id>/', views.excluir_medidor, name='excluir_medidor'),
]
