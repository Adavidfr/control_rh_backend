# EJEMPLOS DE USO DE LA API - SISTEMA RH

## 1. AUTENTICACIÓN

### Registrar nuevo usuario

```bash
POST /api/auth/register/
Content-Type: application/json

{
  "username": "jgarcia",
  "email": "jgarcia@empresa.com",
  "password": "segura123",
  "password_confirm": "segura123",
  "first_name": "Juan",
  "last_name": "García"
}
```

Respuesta:

```json
{
  "user": {
    "id": 1,
    "username": "jgarcia",
    "email": "jgarcia@empresa.com",
    "first_name": "Juan",
    "last_name": "García"
  },
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "access": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

### Login

```bash
POST /api/auth/login/
Content-Type: application/json

{
  "username": "jgarcia",
  "password": "segura123"
}
```

---

## 2. DEPARTAMENTOS

### Crear departamento

```bash
POST /api/departamentos/
Authorization: Bearer {access_token}
Content-Type: application/json

{
  "code": "TI",
  "nombre": "Tecnología de la Información",
  "descripcion": "Departamento de sistemas e infraestructura",
  "presupuesto_anual": 50000.00,
  "jefe_departamento": "Juan García",
  "is_active": true
}
```

### Listar departamentos activos

```bash
GET /api/departamentos/activos/
Authorization: Bearer {access_token}
```

---

## 3. PUESTOS

### Crear puesto

```bash
POST /api/puestos/
Authorization: Bearer {access_token}
Content-Type: application/json

{
  "code": "DEV001",
  "titulo": "Desarrollador Python Senior",
  "descripcion": "Desarrollo backend en Python/Django",
  "salario_base": 2000.00,
  "salario_maximo": 3000.00,
  "departamento": 1,
  "requisitos": "5+ años experiencia Python, PostgreSQL, REST APIs",
  "is_active": true
}
```

### Consultar rango de salarios

```bash
GET /api/puestos/salarios_rango/
Authorization: Bearer {access_token}
```

---

## 4. EMPLEADOS

### Crear empleado

```bash
POST /api/empleados/
Authorization: Bearer {access_token}
Content-Type: application/json

{
  "numero_empleado": "EMP001",
  "cedula": "1234567890",
  "nombre": "Carlos",
  "apellido": "López",
  "edad": 30,
  "email": "carlos.lopez@empresa.com",
  "telefono": "+34 600 123 456",
  "direccion": "Calle Principal 123, Piso 2",
  "fecha_nacimiento": "1994-05-15",
  "fecha_ingreso": "2020-01-15",
  "salario_actual": 2200.00,
  "tipo_contrato": "indefinido",
  "status": "activo",
  "puesto": 1,
  "departamento": 1,
  "supervisor": null,
  "notas": "Excelente desempeño"
}
```

### Listar empleados activos

```bash
GET /api/empleados/activos/
Authorization: Bearer {access_token}
```

### Buscar empleado

```bash
GET /api/empleados/?search=carlos&status=activo
Authorization: Bearer {access_token}
```

### Ver historial de nóminas de un empleado

```bash
GET /api/empleados/1/historial_nominas/
Authorization: Bearer {access_token}
```

### Ver historial de asistencia de un empleado

```bash
GET /api/empleados/1/historial_asistencia/
Authorization: Bearer {access_token}
```

### Ver empleados por departamento

```bash
GET /api/empleados/por_departamento/
Authorization: Bearer {access_token}

Respuesta:
[
  {
    "departamento__nombre": "Tecnología de la Información",
    "total": 5
  },
  {
    "departamento__nombre": "Recursos Humanos",
    "total": 3
  }
]
```

---

## 5. NÓMINAS

### Crear nómina

```bash
POST /api/nominas/
Authorization: Bearer {access_token}
Content-Type: application/json

{
  "empleado": 1,
  "mes": 6,
  "año": 2024,
  "salario_base": 2200.00,
  "bono": 200.00,
  "descuentos": 50.00,
  "descuento_aporte_empleado": 220.00,
  "descuento_impuestos": 180.00,
  "salario_neto": 1950.00,
  "status": "generada",
  "observaciones": "Bonificación por desempeño"
}
```

### Consultar nóminas de un mes específico

```bash
GET /api/nominas/por_mes/?mes=6&año=2024
Authorization: Bearer {access_token}
```

### Ver estadísticas de nómina

```bash
GET /api/nominas/estadisticas/
Authorization: Bearer {access_token}

Respuesta:
{
  "total_empleados_pagados": 45,
  "total_pagado": 125000.00,
  "promedio_salario": 2777.78,
  "total_bonos": 5000.00
}
```

### Marcar nómina como pagada

```bash
PATCH /api/nominas/1/marcar_pagada/
Authorization: Bearer {access_token}
```

---

## 6. ASISTENCIA

### Registrar asistencia (entrada)

```bash
POST /api/asistencias/
Authorization: Bearer {access_token}
Content-Type: application/json

{
  "empleado": 1,
  "fecha": "2024-06-01",
  "status": "presente",
  "hora_entrada": "08:00:00",
  "minutos_retardo": 0,
  "observaciones": "Entrada normal"
}
```

### Registrar salida

```bash
PATCH /api/asistencias/1/registrar_salida/
Authorization: Bearer {access_token}

{
  "hora_salida": "17:30:00"
}
```

### Ver asistencias de una fecha específica

```bash
GET /api/asistencias/por_fecha/?fecha=2024-06-01
Authorization: Bearer {access_token}
```

### Ver empleados presentes hoy

```bash
GET /api/asistencias/presentes_hoy/
Authorization: Bearer {access_token}
```

### Resumen de asistencia de un mes

```bash
GET /api/asistencias/resumen_mes/?mes=6&año=2024
Authorization: Bearer {access_token}

Respuesta:
[
  {
    "status": "presente",
    "count": 20
  },
  {
    "status": "ausente",
    "count": 2
  },
  {
    "status": "retardo",
    "count": 1
  }
]
```

---

## 7. USUARIO ACTUAL

### Obtener información del usuario logueado

```bash
GET /api/auth/me/
Authorization: Bearer {access_token}
```

### Actualizar información del usuario

```bash
PATCH /api/auth/me/
Authorization: Bearer {access_token}
Content-Type: application/json

{
  "first_name": "Juan",
  "email": "juan@empresa.com"
}
```

---

## 8. HEALTH CHECK

### Verificar estado de la API

```bash
GET /api/health/

Respuesta:
{
  "status": "ok",
  "service": "Sistema de Control de Recursos Humanos",
  "version": "1.0.0"
}
```

---

## FILTRADO Y BÚSQUEDA

### Filtrar empleados por estado

```bash
GET /api/empleados/?status=activo
GET /api/empleados/?status=en_licencia
GET /api/empleados/?status=inactivo
```

### Filtrar empleados por departamento

```bash
GET /api/empleados/?departamento=1
```

### Filtrar empleados por puesto

```bash
GET /api/empleados/?puesto=1
```

### Buscar empleado por nombre

```bash
GET /api/empleados/?search=Carlos
```

### Búsqueda combinada

```bash
GET /api/empleados/?status=activo&departamento=1&search=Carlos&page=1&page_size=20
```

---

## PAGINACIÓN

### Solicitar página específica

```bash
GET /api/empleados/?page=2
```

### Cambiar tamaño de página

```bash
GET /api/empleados/?page_size=50
```

### Combinación

```bash
GET /api/empleados/?page=3&page_size=25
```

---

## ORDENAMIENTO

### Ordenar por apellido (ascendente)

```bash
GET /api/empleados/?ordering=apellido
```

### Ordenar descendente

```bash
GET /api/empleados/?ordering=-salario_actual
```

---

## RESPUESTAS DE ERROR

### Falta de autenticación

```json
{
  "detail": "Las credenciales de autenticación no se proporcionaron."
}
```

### Token inválido

```json
{
  "detail": "Token inválido o expirado"
}
```

### Validación fallida

```json
{
  "email": ["Este campo debe ser único."],
  "cedula": ["Este campo es obligatorio."]
}
```

### Recurso no encontrado

```json
{
  "detail": "No encontrado."
}
```

---

## NOTAS IMPORTANTES

- ✅ Todos los endpoints requieren autenticación JWT (excepto login, register y health)
- ✅ Los tokens JWT tienen una duración limitada
- ✅ Usar el token refresh para obtener nuevo access token
- ✅ Las búsquedas son insensibles a mayúsculas/minúsculas
- ✅ Paginación por defecto: 20 resultados por página
- ✅ Máximo 100 resultados por página
- ✅ Las nóminas y asistencias son únicas por (empleado, período)
