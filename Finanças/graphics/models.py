from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model



#Tabela recebe -> Usuário | Data | Valor
# Data -> Referente ao valor recebido
class Gain(models.Model):
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    data = models.DateField()
    valor = models.DecimalField('Valor', max_digits=8, decimal_places=2)
    origem = models.CharField('Origem do valor', max_length=150, blank=True)
    
    def __str__(self):
        return str(self.usuario)

class Lose(models.Model):
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    data = models.DateField()
    valor = models.DecimalField('Valor', max_digits=8, decimal_places=2)
    credor = models.CharField('Credor', max_length=300)

    def __str__(self):
        return str(self.usuario)

class Financa(models.Model):
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    valor = models.DecimalField('Valor', max_digits=8, decimal_places=2)
    dividido = models.IntegerField('Dividido em quantas vezes', default=1)
    inicio = models.DateField('Mês em que se iniciou a Dívida')
    credor = models.CharField('Função do pagamento', max_length=300)
    descricao = models.CharField('Descrição', blank=True, max_length=400)

    def __str__(self):
        return str(self.usuario)


