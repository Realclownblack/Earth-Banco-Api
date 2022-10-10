from turtle import update
from django.shortcuts import render
from cgitb import lookup, reset
from email.policy import HTTP
from math import prod
from re import T
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Cartoes, Cliente, Conta, Contato, Emprestimos, Endereco, Extrato, Fatura, Imagens, Pagamento_Emprstimos, Tranferencia, Usuario
from .serializer import CartoesSerializer, ContaSerializer, ContatoSerializer, EmprestimosSerializer, EnderecoSerializer, ExtratoSerializer, FaturaSerializer, ImagensSerializer, Pagamento_EmprstimosSerializer, RegisterClienteSerializer, RegisterUsuarioSerializer, TransferenciaSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import viewsets
import random
from random import randint

class ImagensViewSet(viewsets.ModelViewSet):
    queryset = Imagens.objects.all()
    serializer_class = ImagensSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = RegisterUsuarioSerializer
    def create(self, request, *args, **kwargs):
        lista_token = []
        listaCaracteries = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                            '1','2','3','4','5','6','7','8','9','#','!','?','$','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
                            'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'z','']
        for i in range(1, 6):
            cod = random.choice(listaCaracteries)
            cod = str(cod)
            lista_token.append(cod)
        value = ''.join(lista_token)
        lista_token.clear()  
        return super().create(request, *args, **kwargs)

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = RegisterClienteSerializer

class ContatoViewSet(viewsets.ModelViewSet):
    queryset = Contato.objects.all()
    serializer_class = ContatoSerializer

class EnderecoViewSet(viewsets.ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer

class ContaViewSet(viewsets.ModelViewSet):
    queryset = Conta.objects.all()
    serializer_class = ContaSerializer
    def create(self, request, *args, **kwargs):
        lista_Account = []
        for i in range(1,7):
            cod = randint(0, 9)
            cod = str(cod)
            lista_Account.append(cod)
        value = ''.join(lista_Account)
        lista_Account.clear()
        request.data['account'] = value
        return super().create(request, *args, **kwargs)

class ExtratoViewSet(viewsets.ModelViewSet):
    queryset = Extrato.objects.all()
    serializer_class = ExtratoSerializer

class CartoesViewSet(viewsets.ModelViewSet):
    queryset =  Cartoes.objects.all()
    serializer_class = CartoesSerializer

    def create(self, request, *args, **kwargs):
        lista_namberCad = []
        for i in range(1, 17):
            cod = randint(0, 9)
            cod = str(cod)
            lista_namberCad.append(cod)
        value = ''.join(lista_namberCad)
        lista_namberCad.clear
        request.data['namber_cad'] = value
        return super().create(request, *args, **kwargs)

class TransferenciaViewSet(viewsets.ModelViewSet):
    queryset =  Tranferencia.objects.all()
    serializer_class = TransferenciaSerializer

class EmprestimosViewSet(viewsets.ModelViewSet):
    queryset =  Emprestimos.objects.all()
    serializer_class = EmprestimosSerializer

class Pagamento_EmprstimosViewSet(viewsets.ModelViewSet):
    queryset =  Pagamento_Emprstimos.objects.all()
    serializer_class = Pagamento_EmprstimosSerializer

class FaturaViewSet(viewsets.ModelViewSet):
    queryset =  Fatura.objects.all()
    serializer_class = FaturaSerializer