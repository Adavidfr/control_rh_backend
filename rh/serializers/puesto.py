# rh/serializers/puesto.py
from rest_framework import serializers
from rh.models import Puesto, Departamento


class PuestoSerializer(serializers.ModelSerializer):
    departamento_nombre = serializers.CharField(source='departamento.nombre', read_only=True)
    empleados_count = serializers.SerializerMethodField()

    class Meta:
        model = Puesto
        fields = [
            'id', 'code', 'titulo', 'descripcion',
            'salario_base', 'salario_maximo', 'salario_promedio',
            'departamento', 'departamento_nombre', 'requisitos',
            'is_active', 'empleados_count', 'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at', 'salario_promedio']

    def get_empleados_count(self, obj):
        return obj.empleados.count()
