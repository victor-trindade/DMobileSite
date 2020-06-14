from django.db import models
from prom.models import Colaborador

CHOICES = (
    ("0", "Responsábilidade"),
    ("1", "Manutenção"),
    ("2", "B.O")
)


class Doc(models.Model):
    tipo = models.CharField(max_length=255, choices=CHOICES)
    img = models.ImageField()
    data = models.DateTimeField()
    colab = models.ForeignKey(Colaborador, on_delete=models.PROTECT)
    def __str__(self):
        try:
            return f'{self.get_tipo_display()} - {self.colab.nome}'
        except:
            return self.get_tipo_display()