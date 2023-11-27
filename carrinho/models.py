from decimal import Decimal
from django.db import models
from django.urls import reverse
from paes.models import Pao

class Carrinho(models.Model):
    pao = models.ForeignKey(Pao, on_delete=models.CASCADE)
    quantidade = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantidade} x {self.pao.descricao}"

    def get_absolute_url(self):
        return reverse("carrinho:carrinho_detail")
    

    @property
    def total(self):
        return round(Decimal(self.pao.valor * self.quantidade), 2)
