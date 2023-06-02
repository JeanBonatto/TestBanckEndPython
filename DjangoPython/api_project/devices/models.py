#Import da biblioteca dos modelos, presente no Django
from django.db import models
# Criação dos modelos.

#Criação do Endpoint do modelo do dispositivo, onde exige o nome e mac_andress
class Dispositivo(models.Model):
    nome = models.CharField(max_length=100)
    mac_address = models.CharField(max_length=17)

    def __str__(self):
        return self.name


#Criação do Endpoint do modelo dos dados de entrada na nossa base
class DadoEntrada(models.Model):
    valor = models.FloatField()
    data_hora = models.DateTimeField()
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.value)