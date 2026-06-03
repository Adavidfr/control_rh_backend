# rh/views/health.py
from rest_framework import views, status
from rest_framework.response import Response


class HealthCheckView(views.APIView):
    """Vista para verificar el estado de la API"""
    
    def get(self, request):
        return Response({
            'status': 'ok',
            'service': 'Sistema de Control de Recursos Humanos',
            'version': '1.0.0'
        }, status=status.HTTP_200_OK)
