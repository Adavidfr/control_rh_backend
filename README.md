# Sistema de Control de Recursos Humanos (RH)

Backend API para la gestión integral de recursos humanos desarrollado con Django REST Framework.

## Características

- ✅ Gestión de Departamentos
- ✅ Gestión de Puestos/Cargos
- ✅ Gestión de Empleados
- ✅ Control de Nóminas
- ✅ Registro de Asistencia
- ✅ Autenticación con JWT
- ✅ Filtrado y búsqueda avanzada
- ✅ Paginación configurable
- ✅ Admin de Django completo

## Los 5 Modelos Principales

### 1. **Departamento**

- Código único
- Nombre y descripción
- Presupuesto anual
- Jefe del departamento
- Estado activo/inactivo

### 2. **Puesto**

- Código único
- Título del cargo
- Rango de salarios (base y máximo)
- Descripción y requisitos
- Asociado a un departamento
- Estado activo/inactivo

### 3. **Empleado**

- Número único de empleado
- Cédula de identidad
- Información personal (nombre, edad, fecha de nacimiento)
- Contacto (email, teléfono, dirección)
- Puesto y departamento
- Salario actual
- Tipo de contrato (indefinido, temporal, practicante, consultor)
- Estado (activo, en licencia, suspendido, inactivo)
- Supervisor y subordinados

### 4. **Nómina**

- Empleado asociado
- Período (mes y año)
- Salario base y bono
- Descuentos (aportes, impuestos)
- Salario neto
- Estado (generada, revisada, pagada, anulada)
- Fecha de generación y pago

### 5. **Asistencia**

- Empleado asociado
- Fecha del registro
- Status (presente, ausente, licencia, retardo, salida anticipada)
- Hora de entrada y salida
- Minutos de retardo
- Observaciones
- Cálculo automático de horas trabajadas

## Instalación

### Requisitos

- Python 3.8+
- PostgreSQL 12+
- pip

### Pasos

1. **Crear entorno virtual**

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

2. **Instalar dependencias**

```bash
pip install -r requirements.txt
```

3. **Ejecutar migraciones**

```bash
python manage.py migrate
```

4. **Crear superusuario**

```bash
python manage.py createsuperuser
```

5. **Iniciar servidor**

```bash
python manage.py runserver
```

## Autenticación (JWT) — Ejemplo de uso

1. Obtener tokens (login):

```bash
curl -X POST http://localhost:8000/api/auth/login/ \
	-H "Content-Type: application/json" \
	-d '{"username":"admin","password":"pass1234"}'
```

Respuesta esperada contiene `access` y `refresh`. Para llamadas protegidas, enviar header:

```
Authorization: Bearer <access_token>
```

2. Refrescar token:

```bash
curl -X POST http://localhost:8000/api/auth/token/refresh/ \
	-H "Content-Type: application/json" \
	-d '{"refresh":"<refresh_token>"}'
```

3. Logout (blacklist de refresh token):

```bash
curl -X POST http://localhost:8000/api/auth/logout/ \
	-H "Content-Type: application/json" \
	-H "Authorization: Bearer <access_token>" \
	-d '{"refresh":"<refresh_token>"}'
```

## Colección Postman

Se agregó una colección mínima para pruebas: `postman_collection_control_rh.json` en la raíz del repositorio. Importe esa colección en Postman o Thunder Client y configure la variable `base_url` (por defecto `http://localhost:8000`).

## Endpoints Principales

### Departamentos

- `GET /api/departamentos/` - Listar
- `POST /api/departamentos/` - Crear
- `GET /api/departamentos/{id}/` - Detalle
- `PUT /api/departamentos/{id}/` - Actualizar (reemplazo completo)
- `PATCH /api/departamentos/{id}/` - Actualizar (parcial)
- `DELETE /api/departamentos/{id}/` - Eliminar
- `GET /api/departamentos/activos/` - Listar departamentos activos
- `GET /api/departamentos/{id}/empleados_total/` - Total de empleados en el departamento (custom)
- `GET /api/departamentos/{id}/puestos_disponibles/` - Puestos disponibles en el departamento (custom)

### Puestos

- `GET /api/puestos/` - Listar
- `POST /api/puestos/` - Crear
- `GET /api/puestos/{id}/empleados_puesto/` - Empleados en el puesto
- `GET /api/puestos/{id}/` - Detalle
- `PUT /api/puestos/{id}/` - Actualizar (reemplazo completo)
- `PATCH /api/puestos/{id}/` - Actualizar (parcial)
- `DELETE /api/puestos/{id}/` - Eliminar
- `GET /api/puestos/activos/` - Listar puestos activos
- `GET /api/puestos/{id}/empleados_puesto/` - Empleados del puesto (custom)
- `GET /api/puestos/salarios_rango/` - Información sobre rangos de salarios (custom)

### Empleados

- `GET /api/empleados/` - Listar
- `POST /api/empleados/` - Crear
- `GET /api/empleados/activos/` - Solo activos
- `GET /api/empleados/{id}/historial_nominas/` - Historial de nóminas
- `GET /api/empleados/{id}/historial_asistencia/` - Historial de asistencia
- `GET /api/empleados/{id}/` - Detalle
- `PUT /api/empleados/{id}/` - Actualizar (reemplazo completo)
- `PATCH /api/empleados/{id}/` - Actualizar (parcial)
- `DELETE /api/empleados/{id}/` - Eliminar
- `GET /api/empleados/por_departamento/` - Empleados agrupados por departamento (custom)
- `GET /api/empleados/{id}/subordinados/` - Subordinados del empleado (custom)

### Nóminas

- `GET /api/nominas/` - Listar
- `POST /api/nominas/` - Crear
- `GET /api/nominas/estadisticas/` - Estadísticas
- `PATCH /api/nominas/{id}/marcar_pagada/` - Marcar como pagada
- `GET /api/nominas/{id}/` - Detalle
- `PUT /api/nominas/{id}/` - Actualizar (reemplazo completo)
- `PATCH /api/nominas/{id}/` - Actualizar (parcial)
- `DELETE /api/nominas/{id}/` - Eliminar
- `GET /api/nominas/por_mes/?mes={m}&año={y}` - Filtrar por mes y año (custom)
- `GET /api/nominas/pagadas/` - Listar nóminas pagadas (custom)

### Asistencia

- `GET /api/asistencias/` - Listar
- `POST /api/asistencias/` - Registrar
- `GET /api/asistencias/presentes_hoy/` - Presentes hoy
- `PATCH /api/asistencias/{id}/registrar_salida/` - Registrar salida
- `GET /api/asistencias/{id}/` - Detalle
- `PUT /api/asistencias/{id}/` - Actualizar (reemplazo completo)
- `PATCH /api/asistencias/{id}/` - Actualizar (parcial)
- `DELETE /api/asistencias/{id}/` - Eliminar
- `GET /api/asistencias/por_fecha/?fecha=YYYY-MM-DD` - Filtrar por fecha (custom)
- `GET /api/asistencias/resumen_mes/?mes={m}&año={y}` - Resumen por mes (custom)

## Testing

```bash
python manage.py test rh.tests
```

## Licencia

MIT
