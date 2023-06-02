#from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Dispositivo, DadoEntrada
from .serializers import SerializadorDisposito, SerializadorDadoEntrada

class DispositivoViewSet(viewsets.ModelViewSet):
    queryset = Dispositivo.objects.all()
    serializer_class = SerializadorDisposito

class DadoEntradaViewSet(viewsets.ModelViewSet):
    queryset = DadoEntrada.objects.all()
    serializer_class = SerializadorDadoEntrada