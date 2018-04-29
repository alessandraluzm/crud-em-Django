from django.contrib import admin
from .models import Produto, Categoria


class ProdutoInline(admin.TabularInline):
    model = Produto

class CategoriaInline(admin.ModelAdmin):
    inlines = [
        ProdutoInline,
    ]


admin.site.register(Produto)
admin.site.register(Categoria, CategoriaInline)