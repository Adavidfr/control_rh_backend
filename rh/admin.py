# rh/admin.py
from django.contrib import admin
from rh.models import Departamento, Puesto, Empleado, Nomina, Asistencia


@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'code', 'jefe_departamento', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['nombre', 'code']
    fieldsets = (
        ('Información General', {'fields': ('code', 'nombre', 'descripcion')}),
        ('Detalles', {'fields': ('presupuesto_anual', 'jefe_departamento', 'is_active')}),
    )


@admin.register(Puesto)
class PuestoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'code', 'departamento', 'salario_base', 'is_active']
    list_filter = ['is_active', 'departamento', 'created_at']
    search_fields = ['titulo', 'code']
    fieldsets = (
        ('Información General', {'fields': ('code', 'titulo', 'descripcion', 'departamento')}),
        ('Salario', {'fields': ('salario_base', 'salario_maximo')}),
        ('Requisitos', {'fields': ('requisitos', 'is_active')}),
    )


@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ['nombre_completo', 'numero_empleado', 'puesto', 'departamento', 'status', 'created_at']
    list_filter = ['status', 'tipo_contrato', 'departamento', 'puesto', 'created_at']
    search_fields = ['nombre', 'apellido', 'numero_empleado', 'cedula', 'email']
    fieldsets = (
        ('Información Personal', {'fields': ('numero_empleado', 'cedula', 'nombre', 'apellido', 'edad', 'fecha_nacimiento')}),
        ('Contacto', {'fields': ('email', 'telefono', 'direccion')}),
        ('Empleo', {'fields': ('puesto', 'departamento', 'supervisor', 'fecha_ingreso', 'salario_actual', 'tipo_contrato')}),
        ('Estado', {'fields': ('status', 'notas')}),
    )


@admin.register(Nomina)
class NominaAdmin(admin.ModelAdmin):
    list_display = ['empleado', 'periodo', 'salario_neto', 'status', 'created_at']
    list_filter = ['status', 'año', 'mes', 'created_at']
    search_fields = ['empleado__nombre', 'empleado__apellido']
    fieldsets = (
        ('Información Básica', {'fields': ('empleado', 'mes', 'año')}),
        ('Salarios', {'fields': ('salario_base', 'bono', 'descuentos', 'descuento_aporte_empleado', 'descuento_impuestos', 'salario_neto')}),
        ('Estado', {'fields': ('status', 'fecha_pago', 'observaciones')}),
    )
    readonly_fields = ['fecha_generacion']


@admin.register(Asistencia)
class AsistenciaAdmin(admin.ModelAdmin):
    list_display = ['empleado', 'fecha', 'status', 'hora_entrada', 'hora_salida', 'horas_trabajadas']
    list_filter = ['status', 'fecha', 'created_at']
    search_fields = ['empleado__nombre', 'empleado__apellido']
    fieldsets = (
        ('Información', {'fields': ('empleado', 'fecha', 'status')}),
        ('Horas', {'fields': ('hora_entrada', 'hora_salida', 'minutos_retardo')}),
        ('Notas', {'fields': ('observaciones',)}),
    )
