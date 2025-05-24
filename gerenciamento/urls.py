from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from escola import views
from sistema_escolar import views

urlpatterns = [
    #aluno
    path('admin/', admin.site.urls),
    path('alunos/', views.aluno_list, name='aluno_list'),
    path('alunos/novo/', views.aluno_create, name='aluno_create'),
    path('alunos/<int:pk>/editar/', views.aluno_update, name='aluno_update'),
    path('alunos/<int:pk>/deletar/', views.aluno_delete, name='aluno_delete'),

    #professor
    path('professores/', views.professor_list, name='professor_list'),
    path('professores/novo/', views.professor_create, name='professor_create'),
    path('professores/<int:pk>/editar/', views.professor_update, name='professor_update'),
    path('professores/<int:pk>/deletar/', views.professor_delete, name='professor_delete'),

    #home
    path('admin/', admin.site.urls),
    path('', include('sistema_escolar.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', views.login_view, name='login'),
    path('professor/dashboard/', views.professor_dashboard, name='professor_dashboard'),
    path('aluno/dashboard/', views.aluno_dashboard, name='aluno_dashboard'),
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),

]
