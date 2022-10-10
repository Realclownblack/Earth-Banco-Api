from django.urls import path, include
from rest_framework import routers
from . import views

rota = routers.DefaultRouter()
rota.register('imagens',views.ImagensViewSet)
rota.register('registerusuario',views.UsuarioViewSet)

urlpatterns = [
   path('',include(rota.urls)),
]