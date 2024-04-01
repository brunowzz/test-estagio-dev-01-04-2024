from django.db import models
from decimal import Decimal

class ConsumoEnergia(models.Model):
   from django.db import models

class ConsumoEnergia(models.Model):
    nome = models.CharField("Nome do Consumidor", max_length=128)
    documento = models.CharField("Documento (CPF/CNPJ)", max_length=128)
    cidade = models.CharField("Cidade", max_length=128)
    estado = models.CharField("Estado", max_length=128)
    consumo_mes_1 = models.DecimalField(max_digits=10, decimal_places=2)
    consumo_mes_2 = models.DecimalField(max_digits=10, decimal_places=2)
    consumo_mes_3 = models.DecimalField(max_digits=10, decimal_places=2)
    tarifa_distribuidora = models.DecimalField(max_digits=10, decimal_places=2)
    TIPO_TARIFA_CHOICES = [
        ("comercial", "Comercial"),
        ("residencial", "Residencial"),
        ("industrial", "Industrial")
    ]
    tipo_tarifa = models.CharField(max_length=20, choices=TIPO_TARIFA_CHOICES)

    def calcular_economia(self):
        consumo_total = self.consumo_mes_1 + self.consumo_mes_2 + self.consumo_mes_3
        consumo_total_decimal = Decimal(float(consumo_total))  
        if consumo_total_decimal < 10000:
            if self.tipo_tarifa == 'residencial':
                desconto = Decimal('0.18')  
            elif self.tipo_tarifa == 'comercial':
                desconto = Decimal('0.16')  
            else:
                desconto = Decimal('0.12')  
        elif 10000 <= consumo_total_decimal <= 20000:
            if self.tipo_tarifa == 'residencial':
                desconto = Decimal('0.22')  
            elif self.tipo_tarifa == 'comercial':
                desconto = Decimal('0.18')  
            else:
                desconto = Decimal('0.15')  
        else:
            if self.tipo_tarifa == 'residencial':
                desconto = Decimal('0.25')  
            elif self.tipo_tarifa == 'comercial':
                desconto = Decimal('0.22')  
            else:
                desconto = Decimal('0.18')  

        economia_mensal = (consumo_total_decimal * desconto) * self.tarifa_distribuidora
        economia_anual = economia_mensal * Decimal('12')  
        cobertura = Decimal('0.9') if consumo_total_decimal < 10000 else (Decimal('0.95') if consumo_total_decimal <= 20000 else Decimal('0.99'))

        return {
            'nome': self.nome,
            'documento': self.documento,
            'cidade': self.cidade,
            'tarifa_distribuidora': self.tarifa_distribuidora,
            'estado': self.estado,
            'economia_anual': economia_anual,
            'economia_mensal': economia_mensal,
            'desconto_aplicado': desconto * Decimal('100'),  
            'cobertura': cobertura * Decimal('100')  
        }
        