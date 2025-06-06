from django import forms
from app.models import Usuario, Veiculo, Venda

# formulario de cadastro
class formulario(forms.ModelForm):
    class Meta: # não precisa de parenteses
        model = Usuario
        fields = ('nome', 'email', 'cep', 'logradouro', 'bairro', 'cidade', 'estado', 'numero', 'senha')
        # renderizando o formulário
    
        # definindo os atributos dos elementos do form
        widgets = {
            'nome' : forms.TextInput(attrs={'type':'text', 'class':'form-input'}),
            'email' : forms.TextInput(attrs={'type':'email', 'class':'form-input'}),
            'cep' : forms.TextInput(attrs={'type':'text', 'class': 'form-input'}),
            'logradouro' : forms.TextInput(attrs={'type':'text', 'class': 'form-input'}),
            'bairro' : forms.TextInput(attrs={'type':'text', 'class': 'form-input'}),
            'cidade' : forms.TextInput(attrs={'type':'text', 'class': 'form-input'}),
            'estado' : forms.TextInput(attrs={'type':'text', 'class': 'form-input'}),
            'numero' : forms.TextInput(attrs={'type':'text', 'class': 'form-input'}),
            'senha' : forms.TextInput(attrs={'type':'password', 'class':'form-input'})
        }

# formuçario para login
class formularioLogin(forms.ModelForm):
    class Meta: 
        model = Usuario
        fields = ('email', 'senha')
        # renderizando o formulário
    
        # definindo os atributos dos elementos do form
        widgets = {
            'email' : forms.TextInput(attrs={'type':'email', 'class':'form-input'}),
            'senha' : forms.TextInput(attrs={'type':'password', 'class':'form-input'})
        }


class VeiculoForm(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = ('marca', 'modelo', 'descricao', 'preco', 'dataFabricacao', 'estoque', 'imagem', 'categoria')

        widgets = {
            'marca' : forms.TextInput(attrs={'type':'text', 'class':'form-input'}),
            'modelo' : forms.TextInput(attrs={'type':'text', 'class':'form-input'}),
            'descricao' : forms.TextInput(attrs={'type':'text', 'class':'form-input'}),
            'preco' : forms.TextInput(attrs={'type':'number', 'class':'form-input'}),
            'dataFabricacao' : forms.TextInput(attrs={'type':'date', 'class':'form-input'}),
            'estoque' : forms.TextInput(attrs={'type':'number', 'class':'form-input'}),
            'imagem' : forms.FileInput(attrs={'accept': 'image/*'}),
            'categoria' : forms.Select(attrs={
                    'placeholder': 'Selecione a Categoria',
                    'class':'form-input'
                })
        }

class checkoutForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = ('numero_cartao', 'validade', 'cvv')

        widgets = {
            'numero_cartao' : forms.TextInput(attrs={'type' : 'text', 'class':'form-input', 'placeholder':'0000 0000 0000 0000'}),
            'validade' : forms.TextInput(attrs={'type' : 'text', 'class':'form-input', 'placeholder':'12/26'}),
            'cvv' : forms.TextInput(attrs={'type' : 'text', 'class':'form-input', 'placeholder':'123'})
        }