# rh/views/empleado.py
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rh.models import Empleado
from rh.serializers import EmpleadoSerializer


class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['status', 'tipo_contrato', 'departamento', 'puesto']
    search_fields = ['nombre', 'apellido', 'numero_empleado', 'cedula', 'email']
    ordering_fields = ['apellido', 'nombre', 'fecha_ingreso', 'salario_actual']
    ordering = ['apellido', 'nombre']

    @action(detail=False, methods=['get'])
    def activos(self, request):
        """Retorna solo empleados activos"""
        queryset = self.queryset.filter(status='activo')
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def por_departamento(self, request):
        """Retorna empleados agrupados por departamento"""
        from django.db.models import Count
        stats = self.queryset.values('departamento__nombre').annotate(
            total=Count('id')
        )
        return Response(list(stats))

    @action(detail=True, methods=['get'])
    def historial_nominas(self, request, pk=None):
        """Retorna historial de nóminas del empleado"""
        empleado = self.get_object()
        nóminas = empleado.nóminas.all()
        from rh.serializers import NominaSerializer
        return Response(NominaSerializer(nóminas, many=True).data)

    @action(detail=True, methods=['get'])
    def historial_asistencia(self, request, pk=None):
        """Retorna historial de asistencia del empleado"""
        empleado = self.get_object()
        asistencias = empleado.asistencias.all()
        from rh.serializers import AsistenciaSerializer
        return Response(AsistenciaSerializer(asistencias, many=True).data)

    @action(detail=True, methods=['get'])
    def subordinados(self, request, pk=None):
        """Retorna empleados bajo supervisión"""
        empleado = self.get_object()
        subordinados = empleado.subordinados.all()
        return Response(self.get_serializer(subordinados, many=True).data)
