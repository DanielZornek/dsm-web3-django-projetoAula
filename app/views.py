from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
from app.models import Usuario

# Create your views here.

def app(request):

    pagina_main = loader.get_template('index.html')

    return HttpResponse(pagina_main.render())

def exibirUsuarios(request):
    usuarios = Usuario.objects.all().values()

    return render(request, "usuarios.html", 
                  {'listaUsuarios': usuarios}) # passando os usuarios como parametro para mostrar eles na pagina
                    # {} PARA PASSAR PARA DICIONARIO PQ VEM COMO ARRAY ASSOCIATIVO