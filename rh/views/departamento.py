# rh/views/departamento.py
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rh.models import Departamento
from rh.serializers import DepartamentoSerializer


class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['is_active']
    search_fields = ['nombre', 'code']
    ordering_fields = ['nombre', 'created_at']
    ordering = ['nombre']

    @action(detail=False, methods=['get'])
    def activos(self, request):
        """Retorna solo departamentos activos"""
        queryset = self.queryset.filter(is_active=True)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def empleados_total(self, request, pk=None):
        """Retorna el número total de empleados en el departamento"""
        departamento = self.get_object()
        return Response({'total_empleados': departamento.empleados.count()})

    @action(detail=True, methods=['get'])
    def puestos_disponibles(self, request, pk=None):
        """Retorna puestos disponibles en el departamento"""
        departamento = self.get_object()
        puestos = departamento.puestos.filter(is_active=True)
        serializer = DjangoFilterBackend().get_serializer(puestos, many=True)
        from rh.serializers import PuestoSerializer
        return Response(PuestoSerializer(puestos, many=True).data)
