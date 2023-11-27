from django.db import models
from django.urls import reverse


class Pao(models.Model):
    nome = models.CharField(max_length=200,)
    descricao = models.CharField(max_length=400,)
    valor = models.DecimalField(decimal_places=2, max_digits=6)

    def __str__(self):
        return f"{self.nome} ({self.descricao})"
    


    def get_fields(self):
        return [
            (field.verbose_name, field.value_from_object(self))
            for field in self.__class__._meta.fields[1:]
            ]
    



