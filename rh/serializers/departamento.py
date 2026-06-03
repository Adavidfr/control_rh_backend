# rh/serializers/departamento.py
from rest_framework import serializers
from rh.models import Departamento


class DepartamentoSerializer(serializers.ModelSerializer):
    empleados_count = serializers.SerializerMethodField()
    puestos_count = serializers.SerializerMethodField()

    class Meta:
        model = Departamento
        fields = [
            'id', 'code', 'nombre', 'descripcion',
            'presupuesto_anual', 'jefe_departamento',
            'is_active', 'empleados_count', 'puestos_count',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']

    def get_empleados_count(self, obj):
        return obj.empleados.count()

    def get_puestos_count(self, obj):
        return obj.puestos.count()
