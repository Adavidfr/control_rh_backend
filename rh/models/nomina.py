# rh/models/nomina.py
from django.db import models
from .empleado import Empleado


class Nomina(models.Model):
    STATUS_CHOICES = [
        ('generada', 'Generada'),
        ('revisada', 'Revisada'),
        ('pagada', 'Pagada'),
        ('anulada', 'Anulada'),
    ]

    empleado = models.ForeignKey(
        Empleado,
        on_delete=models.PROTECT,
        related_name='nóminas',
    )
    mes = models.PositiveIntegerField()  # 1-12
    año = models.PositiveIntegerField()
    salario_base = models.DecimalField(max_digits=12, decimal_places=2)
    bono = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    descuentos = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    descuento_aporte_empleado = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    descuento_impuestos = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    salario_neto = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='generada')
    fecha_generacion = models.DateTimeField(auto_now_add=True)
    fecha_pago = models.DateTimeField(null=True, blank=True)
    observaciones = models.TextField(blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-año', '-mes']
        unique_together = ['empleado', 'mes', 'año']
        verbose_name_plural = 'Nóminas'

    def __str__(self):
        return f'Nómina {self.empleado.nombre_completo} — {self.mes}/{self.año}'

    @property
    def periodo(self):
        meses = {
            1: 'Enero', 2: 'Febrero', 3: 'Marzo', 4: 'Abril',
            5: 'Mayo', 6: 'Junio', 7: 'Julio', 8: 'Agosto',
            9: 'Septiembre', 10: 'Octubre', 11: 'Noviembre', 12: 'Diciembre'
        }
        return f'{meses.get(self.mes, "")} {self.año}'

    @property
    def total_descuentos(self):
        return round(
            float(self.descuentos) +
            float(self.descuento_aporte_empleado) +
            float(self.descuento_impuestos),
            2
        )

    @property
    def bruto(self):
        return round(float(self.salario_base) + float(self.bono), 2)
