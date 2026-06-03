# rh/serializers/empleado.py
from rest_framework import serializers
from rh.models import Empleado


class EmpleadoSerializer(serializers.ModelSerializer):
    puesto_titulo = serializers.CharField(source='puesto.titulo', read_only=True)
    departamento_nombre = serializers.CharField(source='departamento.nombre', read_only=True)
    supervisor_nombre = serializers.CharField(source='supervisor.nombre_completo', read_only=True, allow_null=True)
    nombre_completo = serializers.CharField(read_only=True)
    full_profile = serializers.CharField(read_only=True)
    salario_con_bonificacion = serializers.DecimalField(max_digits=12, decimal_places=2, read_only=True)
    dias_en_empresa = serializers.IntegerField(read_only=True)

    class Meta:
        model = Empleado
        fields = [
            'id', 'numero_empleado', 'cedula', 'nombre', 'apellido',
            'nombre_completo', 'full_profile', 'edad', 'email', 'telefono',
            'direccion', 'fecha_nacimiento', 'fecha_ingreso', 'dias_en_empresa',
            'salario_actual', 'salario_con_bonificacion', 'tipo_contrato',
            'status', 'puesto', 'puesto_titulo', 'departamento',
            'departamento_nombre', 'supervisor', 'supervisor_nombre',
            'notas', 'created_at', 'updated_at'
        ]
        read_only_fields = [
            'created_at', 'updated_at', 'nombre_completo',
            'full_profile', 'salario_con_bonificacion', 'dias_en_empresa'
        ]
