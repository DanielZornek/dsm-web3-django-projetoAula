from django.db import models

# Create your models here.
class Usuario(models.Model): # aqui dizemos que a classe pai Model irá dar herança para a classe usuario
    nome = models.CharField(max_length=100) # varchar, deve especificar o tamanho
    email = models.EmailField()
    senha = models.CharField(max_length=16)
    