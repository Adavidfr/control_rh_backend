# rh/models/empleado.py
from django.db import models
from .puesto import Puesto
from .departamento import Departamento


class Empleado(models.Model):
    STATUS_CHOICES = [
        ('activo', 'Activo'),
        ('en_licencia', 'En Licencia'),
        ('suspendido', 'Suspendido'),
        ('inactivo', 'Inactivo'),
    ]

    TIPO_CONTRATO_CHOICES = [
        ('indefinido', 'Indefinido'),
        ('temporal', 'Temporal'),
        ('practicante', 'Practicante'),
        ('consultor', 'Consultor'),
    ]

    numero_empleado = models.CharField(max_length=20, unique=True)
    cedula = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=120)
    apellido = models.CharField(max_length=120)
    edad = models.PositiveIntegerField()
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True, default='')
    direccion = models.TextField(blank=True, default='')
    fecha_nacimiento = models.DateField()
    fecha_ingreso = models.DateField()
    salario_actual = models.DecimalField(max_digits=12, decimal_places=2)
    tipo_contrato = models.CharField(max_length=20, choices=TIPO_CONTRATO_CHOICES, default='indefinido')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='activo')
    puesto = models.ForeignKey(
        Puesto,
        on_delete=models.PROTECT,
        related_name='empleados',
    )
    departamento = models.ForeignKey(
        Departamento,
        on_delete=models.PROTECT,
        related_name='empleados',
    )
    supervisor = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='subordinados',
    )
    notas = models.TextField(blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['apellido', 'nombre']
        verbose_name_plural = 'Empleados'

    def __str__(self):
        return f'{self.nombre} {self.apellido} ({self.numero_empleado})'

    @property
    def nombre_completo(self):
        return f'{self.nombre} {self.apellido}'

    @property
    def full_profile(self):
        return f'{self.nombre_completo} — {self.puesto.titulo}'

    @property
    def salario_con_bonificacion(self):
        return round(float(self.salario_actual) * 1.10, 2)

    @property
    def dias_en_empresa(self):
        from datetime import date
        return (date.today() - self.fecha_ingreso).days
