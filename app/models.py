from django.db import models

# Create your models here.
class Usuario(models.Model): # aqui dizemos que a classe pai Model irá dar herança para a classe usuario
    nome = models.CharField(max_length=100) # varchar, deve especificar o tamanho
    email = models.EmailField()
    senha = models.CharField(max_length=16)

class Veiculo(models.Model):
    marca = models.CharField(max_length=80)
    modelo = models.CharField(max_length=80)
    descricao = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    dataFabricacao = models.DateField()
    estoque = models.IntegerField()
    imagem = models.ImageField(upload_to='imagens/')