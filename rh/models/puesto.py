# rh/models/puesto.py
from django.db import models
from .departamento import Departamento


class Puesto(models.Model):
    code = models.CharField(max_length=50, unique=True)
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True, default='')
    salario_base = models.DecimalField(max_digits=12, decimal_places=2)
    salario_maximo = models.DecimalField(max_digits=12, decimal_places=2)
    departamento = models.ForeignKey(
        Departamento,
        on_delete=models.PROTECT,
        related_name='puestos',
    )
    requisitos = models.TextField(blank=True, default='')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['titulo']
        verbose_name_plural = 'Puestos'

    def __str__(self):
        return f'{self.titulo} ({self.code})'

    @property
    def full_info(self):
        return f'{self.titulo} — {self.departamento.nombre}'

    @property
    def salario_promedio(self):
        return round((float(self.salario_base) + float(self.salario_maximo)) / 2, 2)
