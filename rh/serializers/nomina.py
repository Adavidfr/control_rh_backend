# rh/serializers/nomina.py
from rest_framework import serializers
from rh.models import Nomina


class NominaSerializer(serializers.ModelSerializer):
    empleado_nombre = serializers.CharField(source='empleado.nombre_completo', read_only=True)
    periodo = serializers.CharField(read_only=True)
    total_descuentos = serializers.DecimalField(max_digits=12, decimal_places=2, read_only=True)
    bruto = serializers.DecimalField(max_digits=12, decimal_places=2, read_only=True)

    class Meta:
        model = Nomina
        fields = [
            'id', 'empleado', 'empleado_nombre', 'mes', 'año', 'periodo',
            'salario_base', 'bono', 'bruto', 'descuentos',
            'descuento_aporte_empleado', 'descuento_impuestos',
            'total_descuentos', 'salario_neto', 'status',
            'fecha_generacion', 'fecha_pago', 'observaciones',
            'created_at', 'updated_at'
        ]
        read_only_fields = [
            'created_at', 'updated_at', 'fecha_generacion',
            'periodo', 'total_descuentos', 'bruto'
        ]
