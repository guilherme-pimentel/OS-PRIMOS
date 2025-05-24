from django import forms
from .models import Aluno
from django.contrib.auth.models import User
from .models import Professor

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['usuario', 'matricula', 'turma', 'contato', 'nome']

class ProfessorForm(forms.ModelForm):
    usuario = forms.ModelChoiceField(
        queryset=User.objects.all(),
        label="Usuário",
        empty_label="Selecione um usuário",
        widget=forms.Select(),
        to_field_name='id',
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['usuario'].label_from_instance = lambda obj: obj.get_full_name() or obj.username

    class Meta:
        model = Professor
        fields = ['usuario', 'contato', 'nome']