from django import forms
from app.models import Usuario

class formulario(forms.ModelForm):
    class Meta: # não precisa de parenteses
        model = Usuario
        fields = ('nome', 'email', 'senha')
        # renderizando o formulário
    
        # definindo os atributos dos elementos do form
        widgets = {
            'nome' : forms.TextInput(attrs={'type':'text', 'class':'form-input'}),
            'email' : forms.TextInput(attrs={'type':'email', 'class':'form-input'}),
            'senha' : forms.TextInput(attrs={'type':'senha', 'class':'form-input'})
        }
