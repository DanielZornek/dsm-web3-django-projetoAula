from datetime import timedelta
from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.template import loader
from django.contrib import messages
from app.models import Usuario, Veiculo
from app.forms import formulario, VeiculoForm, formularioLogin

# Create your views here.

def app(request):

    pagina_main = loader.get_template('index.html')

    return HttpResponse(pagina_main.render())

def exibirUsuarios(request):
    if not request.session.get("email"):    
        return redirect("login")
    usuarios = Usuario.objects.all().values()

    return render(request, "usuarios.html", 
                  {'listaUsuarios': usuarios}) # passando os usuarios como parametro para mostrar eles na pagina
                    # {} PARA PASSAR PARA DICIONARIO PQ VEM COMO ARRAY ASSOCIATIVO

def addUsuario(request):
    formUsuario = formulario(request.POST or None) # verifica se foi ou não submetido

    if request.POST: 
        if formUsuario.is_valid():
            formUsuario.save() # insert
            return redirect("exibirUsuarios")

    return render(request, "add-usuario.html", {'form': formUsuario}) # aspas simples no dicionário

def excluirUsuario(request, id_usuario): # o parametro que a funnção recebe tem de ter o mesmo nome da url
    usuario = Usuario.objects.get(id=id_usuario)
    usuario.delete()
    return redirect('exibirUsuarios')

def editarUsuario(request, id_usuario):
    usuario = Usuario.objects.get(id=id_usuario)
    formUsuarioEditar = formulario(request.POST or None, instance=usuario)

    if request.POST:
        if formUsuarioEditar.is_valid():
            formUsuarioEditar.save()
            return redirect("exibirUsuarios")
    else:
        return render(request, "editar-usuario.html", {'form' : formUsuarioEditar})

def exibirProdutos(request):
    if not request.session.get("email"):    
        return redirect("login")

    veiculos = Veiculo.objects.all().values()
    
    return render(request, "produtos.html", 
                    {'listaProdutos': veiculos})

def cadastrarProduto(request):

    if not request.session.get("email"):    
        return redirect("login")

    form = VeiculoForm(request.POST or None)

    if request.method == 'POST':

        form = VeiculoForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("exibirProdutos")
    
    return render(request, "cadastrar-produto.html", {'formProduto' : form})

def login(request):
    frmLogin = formularioLogin(request.POST or None)

    if request.POST: # ao clicar em entrar, no botão submit do form
        if frmLogin.is_valid():
            _email = frmLogin.cleaned_data.get("email") # capture o email: importante ter algo diferente pra diferencia do atributo da classe do modelo
            _senha = frmLogin.cleaned_data.get("senha") # capture a senha

            try:
                userLogin = Usuario.objects.get(email=_email, senha=_senha) 
                if userLogin is not None:
                    request.session.set_expiry(timedelta(seconds=180))
                    request.session['email'] = _email
                    return redirect("dashboard")
            except Usuario.DoesNotExist:
                return render(request, "login.html")

    return render(request, "login.html", {'form' : frmLogin})

def dashboard(request):
    if not request.session.get("email"):    
        return redirect("login")

    _email = request.session.get("email")
    return render(request, "dashboard.html", {'email': _email})