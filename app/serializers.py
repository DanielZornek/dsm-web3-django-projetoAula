from rest_framework import serializers
from .models import Categoria, Veiculo

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('id', 'nome')

class VeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veiculo
        fields = ('id', 'marca', 'modelo', 'descricao', 'preco', 'dataFabricacao', 'imagem', 'estoque')