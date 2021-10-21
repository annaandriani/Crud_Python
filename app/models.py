from django.db import models


class Ajuda(models.Model):
    nome = models.CharField(max_length=30)
    telefone = models.CharField(max_length=30)
    email = models.CharField(max_length=30)