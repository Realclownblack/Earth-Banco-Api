from django.urls import path, include
from rest_framework import routers
from . import views

rota = routers.DefaultRouter()
rota.register('imagens',views.ImagensViewSet)
rota.register('registercliente',views.ClienteViewSet)

urlpatterns = [
   path('',include(rota.urls)),
   path('registerusuario/', views.RegisterUsuario)
]