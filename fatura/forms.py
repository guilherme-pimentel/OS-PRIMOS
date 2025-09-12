from django import forms
from .models import Fatura

class FaturaForm(forms.ModelForm):
    class Meta:
        model = Fatura
        fields = ['data', 'valor', 'matricula', 'data_vencimento', 'data_pagamento']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
            'data_vencimento': forms.DateInput(attrs={'type': 'date'}),
            'data_pagamento': forms.DateInput(attrs={'type': 'date'}),
        }
