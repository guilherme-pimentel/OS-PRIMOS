from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_matricula, name='lista_matriculas'),
    path('adicionar/', views.adicionar_matricula, name='adicionar_matricula'),
    path('editar/<int:id>/', views.editar_matricula, name='editar_matricula'),
     path('detalhe/<int:id>/', views.detalhe_matricula, name='detalhe_matricula'),
    path('excluir/<int:id>/', views.excluir_matricula, name='excluir_matricula'),
]