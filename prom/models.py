from django.db import models

# Create your models here.

class Colaborador (models.Model):
    nome = models.CharField(max_length=255, verbose_name='Nome')
    uf = models.CharField(max_length=2, verbose_name='UF')


    def __str__(self):
        return self.nome