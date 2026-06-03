# rh/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView
from rh.views import (
    DepartamentoViewSet, PuestoViewSet, EmpleadoViewSet,
    NominaViewSet, AsistenciaViewSet, LoginView, RegisterView,
    LogoutView, UserView, HealthCheckView
)

router = DefaultRouter()
router.register(r'departamentos', DepartamentoViewSet, basename='departamento')
router.register(r'puestos', PuestoViewSet, basename='puesto')
router.register(r'empleados', EmpleadoViewSet, basename='empleado')
router.register(r'nominas', NominaViewSet, basename='nomina')
router.register(r'asistencias', AsistenciaViewSet, basename='asistencia')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/login/', LoginView.as_view(), name='login'),
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/logout/', LogoutView.as_view(), name='logout'),
    path('auth/me/', UserView.as_view(), name='user'),
    # Allow calls without trailing slash (helpers for clients that omit slash)
    path('auth/login', LoginView.as_view()),
    path('auth/register', RegisterView.as_view()),
    path('auth/logout', LogoutView.as_view()),
    path('auth/me', UserView.as_view()),
    # Token refresh/verify (with and without trailing slash)
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/token/refresh', TokenRefreshView.as_view()),
    path('auth/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('auth/token/verify', TokenVerifyView.as_view()),
    path('health/', HealthCheckView.as_view(), name='health'),
]
