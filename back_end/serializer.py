from dataclasses import fields
from decimal import Decimal
from pyexpat import model
from rest_framework import serializers
from .models import Cartoes, Cliente, Conta, Contato, Emprestimos, Endereco, Extrato, Fatura, Imagens, Pagamento_Emprstimos, Tranferencia, Usuario


class ImagensSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagens
        fields = ['id','title','foto']

class RegisterUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['cpf','password','token']

class RegisterClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['name','sex','birthdate','status','usuario']

class ContatoSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Contato
        fields = ['telephone','email','cliente']

class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Endereco
        fields = ['road','number','cep','city','state','district','complement','cliente']

class ContaSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Conta
        fields = ['agency','account','balance','cliente']

class ExtratoSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Extrato
        fields = ['date','value','time','type','conclusion','conta']

class CartoesSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Cartoes
        fields = ['namber_cad','cvc2','date_vale','type_card','flag','nfc','blocked','conta']

class TransferenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Tranferencia
        fields = ['date_movement','type','value','debited','credited']

class EmprestimosSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Emprestimos
        fields = ['velue','date_contract','installments','installments_paind','fees','status']

class Pagamento_EmprstimosSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Pagamento_Emprstimos
        fields = ['amount_to_pay','date_pay','expiration_date','emprestimo']

class FaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Fatura
        fields = ['invoice_amount','expiration_date','fees','cartoes']