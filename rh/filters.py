# rh/filters.py
import django_filters
from rh.models import Empleado, Nomina, Asistencia


class EmpleadoFilter(django_filters.FilterSet):
    nombre = django_filters.CharFilter(field_name='nombre', lookup_expr='icontains')
    apellido = django_filters.CharFilter(field_name='apellido', lookup_expr='icontains')
    departamento = django_filters.CharFilter(field_name='departamento__nombre', lookup_expr='icontains')
    puesto = django_filters.CharFilter(field_name='puesto__titulo', lookup_expr='icontains')
    
    class Meta:
        model = Empleado
        fields = ['status', 'tipo_contrato', 'departamento', 'puesto']


class NominaFilter(django_filters.FilterSet):
    empleado = django_filters.CharFilter(field_name='empleado__nombre', lookup_expr='icontains')
    mes = django_filters.NumberFilter()
    año = django_filters.NumberFilter()
    
    class Meta:
        model = Nomina
        fields = ['status', 'mes', 'año']


class AsistenciaFilter(django_filters.FilterSet):
    empleado = django_filters.CharFilter(field_name='empleado__nombre', lookup_expr='icontains')
    fecha = django_filters.DateFromToRangeFilter()
    
    class Meta:
        model = Asistencia
        fields = ['status', 'fecha']
