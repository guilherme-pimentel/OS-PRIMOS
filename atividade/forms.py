from django import forms
from .models import Atividade

class AtividadeForm(forms.ModelForm):
    class Meta:
        model = Atividade
        fields = ['nome', 'hora', 'funcionario']
        widgets = {
            'hora': forms.TimeInput(attrs={'type': 'time'}),
        }

    def __init__(self, *args, **kwargs):
        super(AtividadeForm, self).__init__(*args, **kwargs)
        self.fields['nome'].label = "Nome da atividade"
        self.fields['hora'].label = "Horário"
        self.fields['funcionario'].label = "Responsável"
