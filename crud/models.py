from django.db import models
from django.db.models import SET_NULL


class Categoria(models.Model):
    nome = models.CharField(max_length=20)
    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    descricao = models.TextField(null=True, blank=True) # Blank pode ou não ser preenchido
    categoria = models.ForeignKey(Categoria, on_delete=SET_NULL, null=True, blank=False)
    def __str__(self):
        return self.nome