# rh/views/puesto.py
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rh.models import Puesto
from rh.serializers import PuestoSerializer


class PuestoViewSet(viewsets.ModelViewSet):
    queryset = Puesto.objects.all()
    serializer_class = PuestoSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['is_active', 'departamento']
    search_fields = ['titulo', 'code']
    ordering_fields = ['titulo', 'salario_base', 'created_at']
    ordering = ['titulo']

    @action(detail=False, methods=['get'])
    def activos(self, request):
        """Retorna solo puestos activos"""
        queryset = self.queryset.filter(is_active=True)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def empleados_puesto(self, request, pk=None):
        """Retorna empleados en este puesto"""
        puesto = self.get_object()
        empleados = puesto.empleados.all()
        from rh.serializers import EmpleadoSerializer
        return Response(EmpleadoSerializer(empleados, many=True).data)

    @action(detail=False, methods=['get'])
    def salarios_rango(self, request):
        """Retorna información sobre rango de salarios"""
        puestos = self.queryset.values(
            'titulo', 'salario_base', 'salario_maximo', 'salario_promedio'
        )
        return Response(list(puestos))
