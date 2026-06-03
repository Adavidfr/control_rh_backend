# rh/models/asistencia.py
from django.db import models
from .empleado import Empleado


class Asistencia(models.Model):
    STATUS_CHOICES = [
        ('presente', 'Presente'),
        ('ausente', 'Ausente'),
        ('licencia', 'Licencia'),
        ('retardo', 'Retardo'),
        ('salida_anticipada', 'Salida Anticipada'),
    ]

    empleado = models.ForeignKey(
        Empleado,
        on_delete=models.PROTECT,
        related_name='asistencias',
    )
    fecha = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='presente')
    hora_entrada = models.TimeField(null=True, blank=True)
    hora_salida = models.TimeField(null=True, blank=True)
    minutos_retardo = models.PositiveIntegerField(default=0)
    observaciones = models.TextField(blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-fecha']
        unique_together = ['empleado', 'fecha']
        verbose_name_plural = 'Asistencias'

    def __str__(self):
        return f'{self.empleado.nombre_completo} — {self.fecha} ({self.status})'

    @property
    def horas_trabajadas(self):
        if self.hora_entrada and self.hora_salida:
            from datetime import datetime
            entrada = datetime.combine(self.fecha, self.hora_entrada)
            salida = datetime.combine(self.fecha, self.hora_salida)
            delta = salida - entrada
            return round(delta.total_seconds() / 3600, 2)
        return 0

    @property
    def es_presente(self):
        return self.status == 'presente'

    @property
    def requiere_justificacion(self):
        return self.status in ['ausente', 'licencia', 'retardo', 'salida_anticipada']
