# rh/models/departamento.py
from django.db import models


class Departamento(models.Model):
    code = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True, default='')
    presupuesto_anual = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    jefe_departamento = models.CharField(max_length=150, blank=True, default='')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['nombre']
        verbose_name_plural = 'Departamentos'

    def __str__(self):
        return f'{self.nombre} ({self.code})'

    @property
    def full_info(self):
        return f'{self.nombre} — {self.code}'
