from datetime import timedelta
from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.template import loader
from app.models import Categoria, Usuario, Veiculo
from app.forms import formulario, VeiculoForm, formularioLogin
import requests
import io, urllib, base64
import matplotlib.pyplot as plt

from app.serializers import CategoriaSerializer, VeiculoSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

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
    viaCEPAPI = requests.get("http://127.0.0.1:8000")
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
    
    return render(request, "produtos.html", {"listaProdutos": veiculos})

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
                    request.session.set_expiry(timedelta(minutes=15))
                    request.session['email'] = _email
                    request.session['nome'] = userLogin.nome
                    return redirect("dashboard")
            except Usuario.DoesNotExist:
                return render(request, "login.html")

    return render(request, "login.html", {'form' : frmLogin})

def dashboard(request):
    if not request.session.get("email"):    
        return redirect("login")

    _email = request.session.get("email")
    _nome = request.session.get("nome")
    return render(request, "dashboard.html", {'email': _email, 'nome': _nome})

def grafico(request):
    # RECUPERA OS DADOS DA TABELA E CRIA DUAS LISTAS
    produtos = Veiculo.objects.all()
    marca_modelo = [f"{v.marca} \n- {v.modelo}" for v in produtos]
    estoque = [v.estoque for v in produtos]

    # CRIA O GRÁFICO EM UMA IMAGEM (COM OS DADOS DAS LISTAS)
    fig, ax = plt.subplots()
    ax.bar(marca_modelo, estoque)
    ax.set_xlabel("Produto")
    ax.set_ylabel("Estoque")
    ax.set_title("Produtos")

    fig.subplots_adjust(bottom=0.2)

    # ARMAZENA A IMAGEM TEMPORARIAMENTE NA MEMÓRIA RAM
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)

    # CONVERTE A IMAGEM EM STRING 
    string = base64.b64encode(buf.read())
    uri = 'data:image/png;base64,' + urllib.parse.quote(string)

    return render(request, 'grafico.html', {'dados' : uri})

@api_view(['GET', 'POST'])
def getCategorias(request):
    if request.method == 'GET':
        categorias = Categoria.objects.all()
        serializer = CategoriaSerializer(categorias, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = CategoriaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def getCategoriaID(request, id_categoria):
    try:
        categoria = Categoria.objects.get(id=id_categoria)
    except Categoria.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = CategoriaSerializer(categoria)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = CategoriaSerializer(categoria, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        categoria.delete()
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def getVeiculos(request):
    if request.method == 'GET':
        categorias = Veiculo.objects.all()
        serializer = VeiculoSerializer(categorias, many=True)
        return Response(serializer.data)