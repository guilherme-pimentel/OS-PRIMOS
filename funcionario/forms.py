from django import forms
from .models import Funcionario

class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ['first_name', 'last_name', 'email', 'cargo', 'salario']

    def save(self, commit=True):
        funcionario = super().save(commit=False)

       
        base_username = (self.cleaned_data['first_name'] + self.cleaned_data['last_name']).lower()
        if not base_username:
            base_username = self.cleaned_data['email'].split('@')[0]

        count = 1
        new_username = base_username
        while Funcionario.objects.filter(username=new_username).exists():
            new_username = f"{base_username}{count}"
            count += 1

        funcionario.username = new_username
        funcionario.set_password("123456") 
        if commit:
            funcionario.save()
        return funcionario