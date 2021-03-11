from django.db import models
from datetime import datetime
from pessoas.models import Pessoas


class Receita(models.Model):
    pessoa = models.ForeignKey(Pessoas, on_delete=models.CASCADE)
    nome_receita = models.CharField(max_length=200)
    ingredientes = models.TextField()  # para criar uma caixa de texto
    modo_preparo = models.TextField()
    tempo_preparo = models.IntegerField()
    rendimento = models.CharField(max_length=50)
    categoria = models.CharField(max_length=100)
    data_postagem = models.DateTimeField(default=datetime.now, blank=True)
    publicado = models.BooleanField(default=False)
    foto_receita = models.ImageField(upload_to='fotos/%m/%Y/', blank=True)

