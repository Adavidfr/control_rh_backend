# INSTRUCCIONES DE INSTALACIÓN Y EJECUCIÓN

## Paso 1: Crear base de datos PostgreSQL

```sql
CREATE DATABASE control_rh;
```

## Paso 2: Instalar dependencias

```bash
pip install -r requirements.txt
```

## Paso 3: Ejecutar migraciones

```bash
# Crear tablas de la aplicación rh
python manage.py migrate

# O si necesitas crear las migraciones primero
python manage.py makemigrations rh
python manage.py migrate rh
```

## Paso 4: Crear superusuario

```bash
python manage.py createsuperuser
```

Ingresa:

- Nombre de usuario
- Email
- Contraseña

## Paso 5: Ejecutar servidor de desarrollo

```bash
python manage.py runserver
```

La API estará disponible en: http://localhost:8000/api/
Panel de administración: http://localhost:8000/admin/

## API Endpoints Disponibles

### Autenticación

- POST /api/auth/login/ - Login
- POST /api/auth/register/ - Registro
- GET /api/auth/me/ - Usuario actual
- POST /api/auth/logout/ - Logout

### Recursos Humanos

- GET/POST /api/departamentos/ - Gestión de departamentos
- GET/POST /api/puestos/ - Gestión de puestos
- GET/POST /api/empleados/ - Gestión de empleados
- GET/POST /api/nominas/ - Gestión de nóminas
- GET/POST /api/asistencias/ - Registro de asistencia

### Salud de la API

- GET /api/health/ - Estado de la API

## Testing

```bash
python manage.py test rh.tests.test_basic -v 2
```

## Estructura de 5 Modelos

1. **Departamento** - Departamentos de la empresa
2. **Puesto** - Cargos y posiciones
3. **Empleado** - Información de empleados
4. **Nómina** - Registros de pago mensual
5. **Asistencia** - Control de entrada/salida

## Notas Importantes

- Usar token JWT para autenticación en endpoints protegidos
- Las nóminas requieren mes y año únicos por empleado
- Las asistencias requieren empleado y fecha únicos
- Todos los modelos tienen timestamps (created_at, updated_at)
- Filtrado y búsqueda disponible en todos los endpoints
