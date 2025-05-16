from django.contrib import admin

from app.models import Usuario, Veiculo

# herdar de admin 
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ("nome", "email") # essa variavel é padrão

class VeiculoAdmin(admin.ModelAdmin):
    list_display = ("marca", "modelo", "preco", "dataFabricacao", "estoque")

# Register your models here.
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Veiculo, VeiculoAdmin)