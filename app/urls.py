from django.urls import path

from . import views

urlpatterns = [
    path('', views.app, name="app"),
    path('usuarios', views.exibirUsuarios, name="exibirUsuarios"), # digitar usuarios para entrar na página na url
    path('add-usuario', views.addUsuario, name="addUsuario"),
    # rota que vai apárecer na url, view, nome
    path('excluir-usuario/<int:id_usuario>', views.excluirUsuario, name="excluirUsuario"),
    path('editar-usuario/<int:id_usuario>', views.editarUsuario, name="editarUsuario"),
    path("cadastrar-produto", views.cadastrarProduto, name="cadastrarProduto"),
    path('produtos', views.exibirProdutos, name="exibirProdutos"),
    path('login', views.login, name="login"),
    path('dashboard', views.dashboard, name="dashboard")
]