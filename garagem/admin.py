from django.contrib import admin

from .models import Veiculo, Acessorio, Cor, Modelo, Categoria, Marca

admin.site.register(Veiculo)
admin.site.register(Acessorio)
admin.site.register(Cor)
admin.site.register(Modelo)
admin.site.register(Categoria)
admin.site.register(Marca)