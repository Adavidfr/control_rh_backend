# rh/views/asistencia.py
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rh.models import Asistencia
from rh.serializers import AsistenciaSerializer


class AsistenciaViewSet(viewsets.ModelViewSet):
    queryset = Asistencia.objects.all()
    serializer_class = AsistenciaSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['status', 'fecha', 'empleado']
    search_fields = ['empleado__nombre', 'empleado__apellido']
    ordering_fields = ['fecha', 'status']
    ordering = ['-fecha']

    @action(detail=False, methods=['get'])
    def por_fecha(self, request):
        """Retorna asistencias de una fecha específica"""
        fecha = request.query_params.get('fecha')
        if fecha:
            queryset = self.queryset.filter(fecha=fecha)
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        return Response({'error': 'Parámetro fecha requerido'}, status=400)

    @action(detail=False, methods=['get'])
    def resumen_mes(self, request):
        """Retorna resumen de asistencia por mes"""
        from django.db.models import Count
        mes = request.query_params.get('mes')
        año = request.query_params.get('año')
        
        if mes and año:
            queryset = self.queryset.filter(
                fecha__month=mes,
                fecha__year=año
            )
            stats = queryset.values('status').annotate(count=Count('id'))
            return Response(list(stats))
        return Response({'error': 'Parámetros mes y año requeridos'}, status=400)

    @action(detail=False, methods=['get'])
    def presentes_hoy(self, request):
        """Retorna empleados presentes hoy"""
        from django.utils import timezone
        hoy = timezone.now().date()
        queryset = self.queryset.filter(fecha=hoy, status='presente')
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['patch'])
    def registrar_salida(self, request, pk=None):
        """Registra la hora de salida"""
        from django.utils import timezone
        asistencia = self.get_object()
        asistencia.hora_salida = timezone.now().time()
        asistencia.save()
        return Response(self.get_serializer(asistencia).data)
