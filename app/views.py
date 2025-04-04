from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.template import loader
from app.models import Usuario
from app.forms import formulario # type: ignore

# Create your views here.

def app(request):

    pagina_main = loader.get_template('index.html')

    return HttpResponse(pagina_main.render())

def exibirUsuarios(request):
    usuarios = Usuario.objects.all().values()

    return render(request, "usuarios.html", 
                  {'listaUsuarios': usuarios}) # passando os usuarios como parametro para mostrar eles na pagina
                    # {} PARA PASSAR PARA DICIONARIO PQ VEM COMO ARRAY ASSOCIATIVO

def addUsuario(request):
    formUser = formulario(request.POST or None) # verifica se foi ou não submetido

    if request.POST: 
        if formUser.is_valid():
            formUser.save() # insert
            return redirect("exibirUsuarios")

    return render(request, "add-usuario.html", {'form': formUser}) # aspas simples no dicionário