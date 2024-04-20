from django.db import models

# Create your models here.

class Produtos(models.Model):
    ID_Produto = models.AutoField(primary_key=True)
    Nome = models.CharField(max_length=100)
    Descricao = models.CharField(max_length=100)
    # Preco = models.DecimalField(max_digits=10, decimal_places=2)
    # Quantidade_Estoque = models.IntegerField()
    Categoria = models.CharField(max_length=100)
    Fornecedor = models.CharField(max_length=100)

    class Meta:
        db_table = 'produtos'

class Funcionarios(models.Model):
    ID_Funcionario = models.AutoField(primary_key=True)
    Nome = models.CharField(max_length=100)
    Senha = models.CharField(max_length=100)
    # Preco = models.DecimalField(max_digits=10, decimal_places=2)
    # Quantidade_Estoque = models.IntegerField()
    Telefone = models.CharField(max_length=100)
    Cargo = models.CharField(max_length=100)

    class Meta:
        db_table = 'funcionarios'