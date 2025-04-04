from django.urls import path

from . import views

urlpatterns = [
    path('', views.app, name="app"),
    path('usuarios', views.exibirUsuarios, name="exibirUsuarios"), # digitar usuarios para entrar na página na url
    path('add-usuario', views.addUsuario, name="addUsuario")
    # rota que vai apárecer na url, view, nome
]