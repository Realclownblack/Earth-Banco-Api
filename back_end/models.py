from django.db import models


class Usuario (models.Model):
    cpf = models.CharField(label=u'CPF')
    password =  models.CharField(min_length = 8,max_length = 8, db_column = 'PASSWORD')
    token = models.CharField(min_length = 5,max_length = 5, db_column = 'Token')

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

    name  = models.CharField(max_length = 100,min_lengtg = 5 , db_column = 'NAME')
    sex = models.CharField(max_length=1,choices=SEX_CHOICE,db_column='SEX')
    birthdate = models.DateField(db_column='BIRTHDATE')
    status = models.CharField(choices=STATUS_CHOICE,db_column='STATUS')

class Contato(models.Model):
    telephone = models.CharField(max_length=11,min_length=11,db_column='TELEPHONE')
    email = models.EmailField(blank=True,null=False , db_column='EMAIL')

class Endereço(models.Model):
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

    road = models.CharField(db_column='ROAD')
    number = models.CharField(max_length=5,min_length=1,db_column='NUMBER')
    cep = models.models.CharField(label=u'CEP')
    city = models.CharField(max_length=255,db_column='CITY')
    state = models.CharField(max_length=2,choices=UF_CHOICES,db_column='STATE')
    district = models.CharField(max_length=255,db_column='DISTRICT')
    complement = models.CharField(max_length=255,db_column='COMPLEMENTE')
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
    value = models.DecimalField(decimal_places=2,db_column='VALUE')
    time = models.TimeField(db_column='TIME',auto_now_add=True)
    type = models.CharField(choices=TYPE_CHOICE,db_column='TYPE')
    conclusion = models.CharField(choices=CONCLUSION_CHOICE,db_column='CONCLUSION')

class Conta(models.Model):
    agency = models.CharField(default='0001',db_column='AGENCY')
    account = models.CharField(max_length = 6,db_column='ACCOUNT')
    balance = models.DecimalField(decimal_places=2,db_column='BALANCE', default = 0.00, max_digits = 30 )
    cliente = models.ForeignKey(Cliente,on_delete=models.PROTECT)
    extrato = models.ForeignKey(Extrato,on_delete=models.PROTECT)

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

    namber_cad = models.IntegerField(max_length=16,min_lengt=16,db_column='NAMBER_CARD')
    cvc2 = models.IntegerField(max_length=4,db_column='CVC2')
    date_vale = models.DateField(db_column='DATE_VALE',auto_now_add=True)
    type_card = models.CharField(db_column='TYPE_CARD',choices=TYPE_CAD_CHOICE)
    flag = models.CharField(db_column='FLAG',choices=FLAG_CHOICE)
    nfc = models.BooleanField(default=True,db_column='NFC')
    blocked = models.BooleanField(default=True,db_column='BLOCKED')

class Tranferencia(models.Model):

    TYPE_CHOICE = (
        ('P', 'PIX'), 
        ('T', 'TRANSFER'),
    )

    date_movement = models.DateField(db_column='DATE_MOVEMENTE',auto_now_add=True)
    type = models.CharField(choices=TYPE_CHOICE,db_column='TYPE')
    value = models.DecimalField(decimal_places=2,db_column='VALUE',default = 0.00,max_digits = 30)
    debited = models.ForeignKey(Conta,on_delete=models.PROTECT)
    credited = models.ForeignKey(Conta,on_delete=models.PROTECT)
  
