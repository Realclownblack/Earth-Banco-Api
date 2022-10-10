from http import client
from django.db import models


class Usuario (models.Model):
    cpf = models.CharField(db_column='CPF',max_length=11)
    password =  models.CharField(max_length = 8, db_column = 'PASSWORD')
    token = models.CharField(max_length = 5, db_column = 'Token')

    def __str__(self) -> str:
        return self.cpf


class Cliente(models.Model):
    SEX_CHOICE = (
        ('m', 'MASCULINO'),
        ('f', 'FEMININO')
    )
    STATUS_CHOICE = (
        ('n', 'NORMAL'),
        ('m', 'MEDIO'),
        ('b', 'BAIXO')
    )

    name = models.CharField(max_length = 100, db_column = 'NAME')
    sex = models.CharField(max_length=1,choices=SEX_CHOICE,db_column='SEX')
    birthdate = models.DateField(db_column='BIRTHDATE')
    status = models.CharField(choices=STATUS_CHOICE,db_column='STATUS',max_length=1)
    usuario = models.ForeignKey(Usuario,on_delete=models.PROTECT)
    

class Contato(models.Model):
    telephone = models.CharField(max_length=11,db_column='TELEPHONE')
    email = models.EmailField(blank=True,null=False , db_column='EMAIL')
    cliente = models.ForeignKey(Cliente,on_delete=models.PROTECT)

class Endereco(models.Model):
    UF_CHOICES = (
        ('AC', 'Acre'), 
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranão'),
        ('MG', 'Minas Gerais'),
        ('MS', 'Mato Grosso do Sul'),
        ('MT', 'Mato Grosso'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PE', 'Pernanbuco'),
        ('PI', 'Piauí'),
        ('PR', 'Paraná'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('RS', 'Rio Grande do Sul'),
        ('SC', 'Santa Catarina'),
        ('SE', 'Sergipe'),
        ('SP', 'São Paulo'),
        ('TO', 'Tocantins')
    )

    road = models.CharField(db_column='ROAD',max_length=5)
    number = models.CharField(max_length=5,db_column='NUMBER')
    cep = models.CharField(db_column ='CEP',max_length=8)
    city = models.CharField(max_length=255,db_column='CITY')
    state = models.CharField(max_length=2,choices=UF_CHOICES,db_column='STATE')
    district = models.CharField(max_length=255,db_column='DISTRICT')
    complement = models.CharField(max_length=255,db_column='COMPLEMENTE')
    cliente = models.ForeignKey(Cliente,on_delete=models.PROTECT)


class Conta(models.Model):
    agency = models.CharField(default='0001',db_column='AGENCY',max_length=4)
    account = models.CharField(max_length = 6,db_column='ACCOUNT')
    balance = models.DecimalField(decimal_places=2,db_column='BALANCE', default = 0.00, max_digits = 30 )
    cliente = models.ForeignKey(Cliente,on_delete=models.PROTECT)
    


class Extrato (models.Model):

    EP_CHOICE = (
        ('ET','EXIT'),
        ('PD','PROHIBITED')
    )

    TYPE_CHOICE = (
        ('P', 'PIX'), 
        ('T', 'TRANSFER'),
        ('D', 'DEPOSIT'),
        ('W', 'WAGE'),
        ('AP', 'ACCOUNT_PAYMENT'),
        ('PA', 'PAYMENT'),
        ('RE', 'REVERSAL')
    )

    CONCLUSION_CHOICE = (
        ('SU','SUCCESS'),
        ('FL','FAILED')
    )


    date = models.DateField(db_column='DATE',auto_now_add=True)
    value = models.DecimalField(decimal_places=2,db_column='VALUE',max_digits=10)
    time = models.TimeField(db_column='TIME',auto_now_add=True)
    type = models.CharField(choices=TYPE_CHOICE,db_column='TYPE',max_length=2)
    conclusion = models.CharField(choices=CONCLUSION_CHOICE,db_column='CONCLUSION',max_length=2)
    conta = models.ForeignKey(Conta,on_delete=models.PROTECT)


class Cartoes(models.Model):

    TYPE_CAD_CHOICE = (
        ('GL','GOLD'),
        ('FR','FREE'),
        ('BL','BLACK'),
        ('PR','PREMIUM'),
        ('GO','GOOD')
    )

    FLAG_CHOICE = (
        ('MT','MASTERCAD'),
        ('VI','VISA'),
        ('EL','ELO')
    )

    namber_cad = models.CharField(max_length=16,db_column='NAMBER_CARD')
    cvc2 = models.CharField(max_length=4,db_column='CVC2')
    date_vale = models.DateField(db_column='DATE_VALE',auto_now_add=True)
    type_card = models.CharField(db_column='TYPE_CARD',choices=TYPE_CAD_CHOICE,max_length=2)
    flag = models.CharField(db_column='FLAG',choices=FLAG_CHOICE,max_length=2)
    nfc = models.BooleanField(default=True,db_column='NFC')
    blocked = models.BooleanField(default=True,db_column='BLOCKED')
    conta = models.ForeignKey(Conta,on_delete=models.PROTECT)


class Tranferencia(models.Model):

    TYPE_CHOICE = (
        ('P', 'PIX'), 
        ('T', 'TRANSFER'),
    )

    date_movement = models.DateField(db_column='DATE_MOVEMENTE',auto_now_add=True)
    type = models.CharField(choices=TYPE_CHOICE,db_column='TYPE',max_length=1)
    value = models.DecimalField(decimal_places=2,db_column='VALUE',default = 0.00,max_digits = 30)
    debited = models.ForeignKey(Conta,on_delete=models.PROTECT,related_name='debited')
    credited = models.ForeignKey(Conta,on_delete=models.PROTECT,related_name='credited')
  
class Emprestimos(models.Model):
    STATUS_CHOICE = (
        ('A','APROVADO'),
        ('R','REPROVADO')
    )

    velue = models.DecimalField(decimal_places=2,db_column='VALUE',default = 0.00,max_digits = 30)
    date_contract = models.DateField(db_column='DATE_VALE', auto_now_add=True)
    installments = models.IntegerField(db_column='INSTALLMENTS')
    installments_paind = models.IntegerField(db_column='INSTALLMENTS_PAIND')
    fees = models.DecimalField(db_column='FEES',default = 0.00,max_digits = 10,decimal_places=2)
    status = models.CharField(db_column='STATUS',choices=STATUS_CHOICE,max_length=1)

class Pagamento_Emprstimos(models.Model):

    amount_to_pay = models.DecimalField(decimal_places=2, db_column='AMOUNT_TO_PAY', default=0.00, max_digits=30)
    date_pay = models.DateField(db_column='DATE_PAY', auto_now_add=True)
    expiration_date = models.DateField(db_column='EXPIRATION_DATE', auto_now_add=True)
    emprestimo = models.ForeignKey(Emprestimos,on_delete=models.PROTECT)


class Fatura(models.Model):

    invoice_amount = models.DecimalField(decimal_places=2, db_column='INVOICE_AMOUNT', default=0.00, max_digits=30)
    expiration_date = models.DateField(db_column='EXPIRATION_DATE', auto_now_add=True)
    fees = models.DecimalField(db_column='FEES', default=0.00, max_digits=10,decimal_places=2)
    cartoes = models.ForeignKey(Cartoes,on_delete=models.PROTECT)



class Imagens(models.Model):
    title = models.CharField(max_length=255)
    foto = models.ImageField(upload_to='back_end/imagens')