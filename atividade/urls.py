from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_atividades, name='lista_atividades'),
    path('adicionar/', views.adicionar_atividade, name='adicionar_atividade'),
    path('editar/<int:id>/', views.editar_atividade, name='editar_atividade'),
    path('excluir/<int:id>/', views.excluir_atividade, name='excluir_atividade'),
    path('detalhe/<int:id>/', views.detalhe_atividade, name='detalhe_atividade'),

]