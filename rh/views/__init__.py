# rh/views/__init__.py
from .departamento import DepartamentoViewSet
from .puesto import PuestoViewSet
from .empleado import EmpleadoViewSet
from .nomina import NominaViewSet
from .asistencia import AsistenciaViewSet
from .auth import LoginView, RegisterView, LogoutView
from .user import UserView
from .health import HealthCheckView
