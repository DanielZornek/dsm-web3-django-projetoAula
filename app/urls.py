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
    path("editar-produto/<int:veiculo_cd>", views.editar_produto, name="editar_produto"),
    path("excluir-produto/<int:veiculo_cd>", views.excluir_produto, name="excluirProduto"), 
    path('produtos', views.exibirProdutos, name="exibirProdutos"),
    path('login', views.login, name="login"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('grafico', views.grafico, name="grafico"),
    path('grafico-vendas', views.graficoVendas, name="graficoVenda"),
    path('categorias', views.getCategorias, name="categorias"),
    path('categorias/<int:id_categoria>', views.getCategoriaID, name="categoriaID"),
    path('veiculos', views.getVeiculos, name="veiculos"),
    path('buscar_cep/', views.buscar_cep_api, name='buscar_cep_api'),
    path('checkout/<int:veiculo_cd>/', views.checkout, name="checkout"),
    path('checkout-status',views.checkout_status, name="checkout_status"),
]