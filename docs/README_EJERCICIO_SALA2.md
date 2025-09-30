# 🏥 Ejercicio Sala 2 - API de Citas GHL

## 📋 Objetivos del Ejercicio

- ✅ Crear cita en GHL con POST `/calendars/events/appointments`
- ✅ Listar citas con GET `/calendars/events/appointments`
- ✅ Guardar appointmentId en estructura local (SQLite)
- ✅ Probar con Postman que la cita aparece en dashboard GHL
- ✅ **PLUS Sala 2:** Implementar PUT para reprogramar citas
- ✅ Documentar pasos y resultados

## 🚀 Configuración Inicial

### 1. Variables de Entorno

Crea un archivo `.env` en la carpeta `backend`:

```env
# GHL API Configuration
GHL_ACCESS_TOKEN=tu_access_token_aqui
GHL_LOCATION_ID=tu_location_id_aqui
GHL_ASSIGNED_USER_ID=tu_assigned_user_id_aqui
GHL_API_VERSION=2021-04-15

# Django Configuration
SECRET_KEY=super-secret-key-change-this
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost,*.ngrok.io
```

### 2. Instalar Dependencias

```bash
cd backend
pip install -r requirements.txt
```

### 3. Ejecutar Migraciones

```bash
python manage.py migrate
```

### 4. Iniciar Servidor

```bash
python manage.py runserver
```

El servidor estará disponible en: `http://127.0.0.1:8000`

## 📱 Configuración de Postman

### 1. Importar Colección

1. Abre Postman
2. Click en "Import"
3. Selecciona el archivo `docs/GHL_API_Collection.postman_collection.json`
4. La colección "GHL API - Sala 2" se importará automáticamente

### 2. Configurar Variables

En Postman, ve a "Environments" y crea un nuevo environment con estas variables:

**Para el Ejercicio Sala 2 (pruebas directas):**

| Variable | Valor | Descripción |
|----------|-------|-------------|
| `base_url` | `http://127.0.0.1:8000` | URL base de tu API local |
| `ghl_token` | `tu_access_token` | Token de GHL |
| `location_id` | `tu_location_id` | ID de ubicación GHL |
| `calendar_id` | `tu_calendar_id` | ID del calendario |
| `contact_id` | `tu_contact_id` | ID del contacto |
| `assigned_user_id` | `tu_user_id` | ID del usuario asignado |
| `ghl_id` | `(se llena automáticamente)` | ID de la cita creada |

**Nota:** Para el ejercicio Sala 2, NO necesitas ngrok. Solo usa la URL local.

## 🧪 Secuencia de Pruebas

### Prueba 1: Crear Cita para Mañana

**Endpoint:** `POST /api/appointments/create/`

**Payload:**
```json
{
  "calendarId": "{{calendar_id}}",
  "contactId": "{{contact_id}}",
  "locationId": "{{location_id}}",
  "assignedUserId": "{{assigned_user_id}}",
  "title": "Cita de Prueba - Mañana",
  "startTime": "2024-01-16T10:00:00Z",
  "endTime": "2024-01-16T11:00:00Z",
  "appointmentStatus": "confirmed",
  "notes": "Cita creada desde Postman - Sala 2"
}
```

**Resultado esperado:**
- Status: `201 Created`
- Respuesta incluye `ghl_id` de la cita creada
- Cita aparece en dashboard de GHL

### Prueba 2: Listar Citas

**Endpoint:** `GET /api/appointments/`

**Resultado esperado:**
- Status: `200 OK`
- Lista de citas incluye la cita creada
- Datos consistentes con la creación

### Prueba 3: Reprogramar Cita (PLUS Sala 2)

**Endpoint:** `PUT /api/appointments/{ghl_id}/update/`

**Payload:**
```json
{
  "title": "Cita Reprogramada - Pasado Mañana",
  "startTime": "2024-01-17T14:00:00Z",
  "endTime": "2024-01-17T15:00:00Z",
  "appointmentStatus": "confirmed",
  "notes": "Cita reprogramada desde Postman - Sala 2"
}
```

**Resultado esperado:**
- Status: `200 OK`
- Nueva fecha y hora en la respuesta
- Cambio reflejado en dashboard de GHL
- **Consistencia:** El `ghl_id` se mantiene igual

### Prueba 4: Verificar Consistencia

**Endpoint:** `GET /api/appointments/`

**Verificaciones:**
- La cita tiene la nueva fecha
- El `ghl_id` se mantiene igual
- Status sigue siendo "confirmed"

## 📊 Verificación en Dashboard GHL

1. **Acceder al Dashboard:**
   - Ve a tu cuenta de GHL
   - Navega a "Calendarios" > "Citas"

2. **Verificar Cita Creada:**
   - ✅ Título: "Cita de Prueba - Mañana"
   - ✅ Fecha: Mañana 10:00-11:00
   - ✅ Estado: Confirmada
   - ✅ Contacto asignado

3. **Verificar Cita Reprogramada:**
   - ✅ Título: "Cita Reprogramada - Pasado Mañana"
   - ✅ Fecha: Pasado mañana 14:00-15:00
   - ✅ Estado: Confirmada
   - ✅ **Mismo ID de cita** (consistencia)

## 🔧 Troubleshooting

### Error 404 - Not Found
- ✅ Verificar que la URL sea correcta
- ✅ Verificar que el servidor Django esté corriendo
- ✅ Verificar que las rutas estén configuradas

### Error 400 - Bad Request
- ✅ Verificar que todos los campos requeridos estén presentes
- ✅ Verificar formato de fechas (ISO 8601)
- ✅ Verificar que los IDs existan en GHL

### Error 500 - Internal Server Error
- ✅ Verificar archivo `.env` con credenciales GHL
- ✅ Verificar token de GHL válido
- ✅ Revisar logs del servidor Django

### Cita no aparece en Dashboard GHL
- ✅ Verificar que el `location_id` sea correcto
- ✅ Verificar que el `calendar_id` sea correcto
- ✅ Verificar que el `contact_id` exista
- ✅ Verificar permisos del token de GHL

## 📈 Resultados Esperados

### ✅ Funcionalidades Base (Todas las Salas)
- [x] Crear cita en GHL
- [x] Listar citas
- [x] Guardar en SQLite local
- [x] Verificar en dashboard GHL

### ✅ Funcionalidades Plus (Sala 2)
- [x] Reprogramar cita con PUT
- [x] Mantener consistencia de ID
- [x] Verificar cambio en dashboard
- [x] Manejar riesgo de consistencia

## 📝 Documentación de Resultados

### Endpoints Implementados

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| POST | `/api/appointments/create/` | Crear cita en GHL |
| GET | `/api/appointments/` | Listar citas |
| PUT | `/api/appointments/{id}/update/` | Actualizar cita |
| DELETE | `/api/appointments/{id}/delete/` | Cancelar cita |

### Estructura de Base de Datos

```sql
-- Tabla appointments
CREATE TABLE appointments_appointment (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ghl_id VARCHAR(255) UNIQUE,
    location_id VARCHAR(255),
    calendar_id VARCHAR(255),
    contact_id VARCHAR(255),
    title VARCHAR(255),
    appointment_status VARCHAR(50),
    assigned_user_id VARCHAR(255),
    notes TEXT,
    start_time DATETIME,
    end_time DATETIME,
    source VARCHAR(100),
    date_added DATETIME,
    date_updated DATETIME
);
```

### Flujo de Datos

1. **Creación:** Postman → Django API → GHL API → SQLite
2. **Listado:** Postman → Django API → SQLite
3. **Actualización:** Postman → Django API → GHL API → SQLite
4. **Verificación:** Dashboard GHL (consistencia)

## 🎯 Conclusión

El ejercicio Sala 2 se ha completado exitosamente con:

- ✅ **Funcionalidades base** implementadas y probadas
- ✅ **Funcionalidades plus** (reprogramación) implementadas
- ✅ **Consistencia de datos** mantenida entre GHL y SQLite
- ✅ **Verificación en dashboard** GHL confirmada
- ✅ **Documentación completa** de pasos y resultados

El sistema maneja correctamente el riesgo de consistencia entre el ID original y la nueva hora, manteniendo la integridad de los datos en ambas plataformas.
