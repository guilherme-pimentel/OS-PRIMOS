from django import forms
from .models import Matricula

class MatriculaForm(forms.ModelForm):
    class Meta:
        model = Matricula
        fields = ['aluno', 'atividade', 'valor', 'data_matricula', 'status']
        widgets = {
            'valor': forms.NumberInput(attrs={'step': '0.01'}),
            'data_matricula': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(MatriculaForm, self).__init__(*args, **kwargs)
        self.fields['aluno'].label = "Aluno"
        self.fields['atividade'].label = "Atividade"
        self.fields['valor'].label = "Valor da matrícula"
        self.fields['data_matricula'].label = "Data da matrícula"
        self.fields['status'].label = "Ativo?"