from django import forms
from app.models import Usuario, Veiculo

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


class VeiculoForm(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = ('marca', 'modelo', 'descricao', 'preco', 'dataFabricacao', 'imagem')

        widgets = {
            'marca' : forms.TextInput(attrs={'type':'text', 'class':'form-input'}),
            'modelo' : forms.TextInput(attrs={'type':'text', 'class':'form-input'}),
            'descricao' : forms.TextInput(attrs={'type':'text', 'class':'form-input'}),
            'preco' : forms.TextInput(attrs={'type':'number', 'class':'form-input'}),
            'dataFabricacao' : forms.TextInput(attrs={'type':'date', 'class':'form-input'}),
            'imagem' : forms.FileInput(attrs={'accept': 'image/*'})
        }