from django.db import models

# Create your models here.
class Usuario(models.Model): # aqui dizemos que a classe pai Model irá dar herança para a classe usuario
    nome = models.CharField(max_length=100) # varchar, deve especificar o tamanho
    email = models.EmailField()
    cep = models.CharField(max_length=10, default="Desconhecida")
    logradouro = models.CharField(max_length=100, default="Desconhecida")
    bairro = models.CharField(max_length=60, default="Desconhecida")
    cidade = models.CharField(max_length=60, default="Desconhecida")
    estado = models.CharField(max_length=3, default="Desconhecida")
    numero = models.CharField(max_length=10, default="Desconhecida")
    senha = models.CharField(max_length=16)

    def __str__(self):
        return f"Nome: {self.nome} | Email: ({self.email})"

# classe que irá se relacionar com Produto para categorias 
class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nome}"

class Veiculo(models.Model):
    marca = models.CharField(max_length=80)
    modelo = models.CharField(max_length=80)
    descricao = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=15, decimal_places=2)
    dataFabricacao = models.DateField()
    estoque = models.IntegerField()
    imagem = models.ImageField(upload_to='imagens/')
    # uma chave primaria(da classe Categoria, o resto é útil quando os produtos já existem e precisam e não tiveram um valor atribuído)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Nome: {self.marca} | Email: ({self.modelo})"

class Venda(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True)
    produto = models.ForeignKey(Veiculo, on_delete=models.SET_NULL, null=True, blank=True)

    preco_venda = models.DecimalField(max_digits=15, decimal_places=2)
    numero_cartao = models.CharField(max_length=25)
    validade = models.CharField(max_length=6)
    cvv = models.CharField(max_length=5)
    data_venda = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        usuario_nome = self.usuario.nome if self.usuario else "Usuário Desconhecido"
        veiculo_modelo = self.produto.modelo if self.produto else "Veículo Desconhecido"
        return f"Venda de {veiculo_modelo} para {usuario_nome}"
