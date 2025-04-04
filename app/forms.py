from django import forms
from app.models import Usuario

class formulario(forms.ModelForm):
    class Meta: # não precisa de parenteses
        model = Usuario
        fields = ('nome', 'email', 'senha')
        # renderizando o formulário
