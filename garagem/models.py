from django.db import models

class Veiculo(models.Model):
    ano = models.IntegerField(blank=True)
    descricao = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=7, decimal_places=2, default=0, null=True, blank=True)

class Acessorio(models.Model):
    descricao = models.CharField(max_length=100)

class Cor(models.Model):
    descricao = models.CharField(max_length=100)
    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Cor"
        verbose_name_plural = "Cores"

class Modelo(models.Model):
    nome = models.CharField(max_length=100)   

class Categoria(models.Model):
    descricao = models.CharField(max_length=100)    

class Marca(models.Model):
    nome = models.CharField(max_length=100)      