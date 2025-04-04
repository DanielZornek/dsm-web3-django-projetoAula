from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader

# Create your views here.

def app(request):

    pagina_main = loader.get_template('index.html')

    return HttpResponse(pagina_main.render())