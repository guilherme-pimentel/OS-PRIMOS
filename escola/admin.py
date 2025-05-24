from django.contrib import admin
from .models import PerfilUsuario, Turma, Professor, Aluno, Disciplina, Nota

admin.site.register(PerfilUsuario)
admin.site.register(Turma)
admin.site.register(Professor)
admin.site.register(Aluno)
admin.site.register(Disciplina)
admin.site.register(Nota)
