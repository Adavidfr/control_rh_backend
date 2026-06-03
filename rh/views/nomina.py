# rh/views/nomina.py
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rh.models import Nomina
from rh.serializers import NominaSerializer


class NominaViewSet(viewsets.ModelViewSet):
    queryset = Nomina.objects.all()
    serializer_class = NominaSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['status', 'mes', 'año', 'empleado']
    search_fields = ['empleado__nombre', 'empleado__apellido']
    ordering_fields = ['año', 'mes', 'fecha_pago']
    ordering = ['-año', '-mes']

    @action(detail=False, methods=['get'])
    def por_mes(self, request):
        """Retorna nóminas de un mes específico"""
        mes = request.query_params.get('mes')
        año = request.query_params.get('año')
        if mes and año:
            queryset = self.queryset.filter(mes=mes, año=año)
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        return Response({'error': 'Parámetros mes y año requeridos'}, status=400)

    @action(detail=False, methods=['get'])
    def estadisticas(self, request):
        """Retorna estadísticas de nómina"""
        from django.db.models import Sum, Count, Avg
        stats = self.queryset.aggregate(
            total_empleados_pagados=Count('empleado', distinct=True),
            total_pagado=Sum('salario_neto'),
            promedio_salario=Avg('salario_neto'),
            total_bonos=Sum('bono'),
        )
        return Response(stats)

    @action(detail=False, methods=['get'])
    def pagadas(self, request):
        """Retorna nóminas pagadas"""
        queryset = self.queryset.filter(status='pagada')
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['patch'])
    def marcar_pagada(self, request, pk=None):
        """Marca la nómina como pagada"""
        from django.utils import timezone
        nomina = self.get_object()
        nomina.status = 'pagada'
        nomina.fecha_pago = timezone.now()
        nomina.save()
        return Response(self.get_serializer(nomina).data)
