from django.contrib import admin

from app.models import Usuario, Veiculo, Categoria

# herdar de admin 
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ("nome", "email") # essa variavel é padrão

class VeiculoAdmin(admin.ModelAdmin):
    list_display = ("marca", "modelo", "preco", "dataFabricacao", "estoque")

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nome",) # sem a virgula da erro

# Register your models here.
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Veiculo, VeiculoAdmin)
admin.site.register(Categoria, CategoriaAdmin)