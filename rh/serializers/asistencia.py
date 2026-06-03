# rh/serializers/asistencia.py
from rest_framework import serializers
from rh.models import Asistencia


class AsistenciaSerializer(serializers.ModelSerializer):
    empleado_nombre = serializers.CharField(source='empleado.nombre_completo', read_only=True)
    horas_trabajadas = serializers.FloatField(read_only=True)
    es_presente = serializers.BooleanField(read_only=True)
    requiere_justificacion = serializers.BooleanField(read_only=True)

    class Meta:
        model = Asistencia
        fields = [
            'id', 'empleado', 'empleado_nombre', 'fecha',
            'status', 'hora_entrada', 'hora_salida',
            'horas_trabajadas', 'minutos_retardo', 'es_presente',
            'requiere_justificacion', 'observaciones',
            'created_at', 'updated_at'
        ]
        read_only_fields = [
            'created_at', 'updated_at', 'horas_trabajadas',
            'es_presente', 'requiere_justificacion'
        ]
