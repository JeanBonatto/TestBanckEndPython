from rest_framework import serializers
from .models import Dispositivo, DadoEntrada

class SerializadorDisposito(serializers.ModelSerializer):
    class Meta:
        model = Dispositivo
        fields = ['id', 'nome', 'mac_address']

class SerializadorDadoEntrada(serializers.ModelSerializer):
    class Meta:
        model = DadoEntrada
        fields = ['id', 'valor', 'data_hora', 'dispositivo']
