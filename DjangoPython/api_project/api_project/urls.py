"""
URL configuration for api_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from devices.views import DispositivoViewSet, DadoEntradaViewSet

router = routers.DefaultRouter()
router.register(r'dispositivo', DispositivoViewSet)
router.register(r'dadoEntrada', DadoEntradaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]

#Rota para Documentação da API
# from rest_framework.documentation import include_docs_urls

# urlpatterns += [
#     path('docs/', include_docs_urls(title='API Documentation')),
# ]
