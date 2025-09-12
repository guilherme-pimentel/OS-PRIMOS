from django import forms
from .models import Avaliacao

class AvaliacaoForm(forms.ModelForm):
    class Meta:
        model = Avaliacao
        fields = ['matricula', 'peso', 'altura', 'avaliador']
        widgets = {
            'peso': forms.NumberInput(attrs={'step': '0.1', 'placeholder': 'Peso em kg'}),
            'altura': forms.NumberInput(attrs={'step': '0.1', 'placeholder': 'Altura em cm'}),
        }

    def __init__(self, *args, **kwargs):
        super(AvaliacaoForm, self).__init__(*args, **kwargs)
        self.fields['matricula'].label = "Matrícula (Aluno - Atividade)"
        self.fields['peso'].label = "Peso (kg)"
        self.fields['altura'].label = "Altura (cm)"
        self.fields['avaliador'].label = "Avaliador"