# 📋 Guía Completa: Postman con GHL API

## 🚀 Configuración Inicial

### 1. Variables de Entorno en Postman

**Para pruebas directas de la API (Ejercicio Sala 2):**

| Variable | Valor | Descripción |
|----------|-------|-------------|
| `base_url` | `http://127.0.0.1:8000` | URL base de tu API local |
| `ghl_token` | `tu_access_token` | Token de acceso de GHL |
| `location_id` | `tu_location_id` | ID de la ubicación en GHL |
| `calendar_id` | `tu_calendar_id` | ID del calendario en GHL |
| `contact_id` | `tu_contact_id` | ID del contacto en GHL |
| `assigned_user_id` | `tu_user_id` | ID del usuario asignado |

**Para webhooks de GHL (opcional):**

| Variable | Valor | Descripción |
|----------|-------|-------------|
| `ngrok_url` | `https://tu-url.ngrok.io` | URL de ngrok para webhooks |
| `webhook_url` | `https://tu-url.ngrok.io/api/webhook/ghl/` | URL del webhook |

### 2. Headers Comunes

Para todas las requests, agrega estos headers:

```
Content-Type: application/json
```

## 📝 Endpoints Disponibles

### 1. 🆕 CREAR CITA (POST)

**URL:** `{{base_url}}/api/appointments/create/`

**Headers:**
```
Content-Type: application/json
```

**Body (JSON):**
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
  "notes": "Cita creada desde Postman"
}
```

**Respuesta esperada:**
```json
{
  "id": 1,
  "ghl_id": "appointment_123456",
  "location_id": "location_123",
  "calendar_id": "calendar_123",
  "contact_id": "contact_123",
  "title": "Cita de Prueba - Mañana",
  "appointment_status": "confirmed",
  "assigned_user_id": "user_123",
  "notes": "Cita creada desde Postman",
  "start_time": "2024-01-16T10:00:00Z",
  "end_time": "2024-01-16T11:00:00Z",
  "source": "api"
}
```

### 2. 📋 LISTAR CITAS (GET)

**URL:** `{{base_url}}/api/appointments/`

**Headers:**
```
Content-Type: application/json
```

**Respuesta esperada:**
```json
[
  {
    "id": 1,
    "ghl_id": "appointment_123456",
    "location_id": "location_123",
    "calendar_id": "calendar_123",
    "contact_id": "contact_123",
    "title": "Cita de Prueba - Mañana",
    "appointment_status": "confirmed",
    "assigned_user_id": "user_123",
    "notes": "Cita creada desde Postman",
    "start_time": "2024-01-16T10:00:00Z",
    "end_time": "2024-01-16T11:00:00Z",
    "source": "api"
  }
]
```

### 3. ✏️ ACTUALIZAR CITA (PUT)

**URL:** `{{base_url}}/api/appointments/{appointment_id}/update/`

**Headers:**
```
Content-Type: application/json
```

**Body (JSON):**
```json
{
  "title": "Cita Reprogramada - Pasado Mañana",
  "startTime": "2024-01-17T14:00:00Z",
  "endTime": "2024-01-17T15:00:00Z",
  "appointmentStatus": "confirmed",
  "notes": "Cita reprogramada desde Postman"
}
```

### 4. 🗑️ CANCELAR CITA (DELETE)

**URL:** `{{base_url}}/api/appointments/{appointment_id}/delete/`

**Headers:**
```
Content-Type: application/json
```

## 🧪 Secuencia de Pruebas (Ejercicio Sala 2)

### Prueba 1: Crear Cita para Mañana

1. **Request:** POST `/api/appointments/create/`
2. **Body:** Usar el JSON de creación con fecha de mañana
3. **Verificar:** 
   - Status 201 Created
   - Guardar el `ghl_id` de la respuesta
   - Verificar en dashboard de GHL

### Prueba 2: Listar Citas

1. **Request:** GET `/api/appointments/`
2. **Verificar:**
   - Status 200 OK
   - La cita creada aparece en la lista
   - Datos consistentes con la creación

### Prueba 3: Reprogramar Cita

1. **Request:** PUT `/api/appointments/{ghl_id}/update/`
2. **Body:** Cambiar fecha a pasado mañana
3. **Verificar:**
   - Status 200 OK
   - Nueva fecha en la respuesta
   - Cambio reflejado en dashboard de GHL

### Prueba 4: Verificar Consistencia

1. **Request:** GET `/api/appointments/`
2. **Verificar:**
   - La cita tiene la nueva fecha
   - El `ghl_id` se mantiene igual
   - Status sigue siendo "confirmed"

## 🔧 Configuración de ngrok

Si necesitas usar ngrok para webhooks:

```bash
# Instalar ngrok
npm install -g ngrok

# Exponer puerto 8000
ngrok http 8000
```

Luego actualiza la variable `ngrok_url` en Postman con la URL que te dé ngrok.

## 📊 Verificación en Dashboard GHL

1. Ve a tu dashboard de GHL
2. Navega a Calendarios > Citas
3. Verifica que las citas aparezcan con:
   - Título correcto
   - Fecha y hora correctas
   - Estado "Confirmada"
   - Contacto asignado

## 🚨 Troubleshooting

### Error 404
- Verificar que la URL sea correcta
- Verificar que el servidor Django esté corriendo

### Error 400
- Verificar que todos los campos requeridos estén presentes
- Verificar formato de fechas (ISO 8601)
- Verificar que los IDs existan en GHL

### Error 500
- Verificar variables de entorno (.env)
- Verificar token de GHL
- Revisar logs del servidor Django

## 📋 Checklist de Verificación

- [ ] Servidor Django corriendo en puerto 8000
- [ ] Archivo .env configurado con credenciales GHL
- [ ] Variables de Postman configuradas
- [ ] Cita creada exitosamente
- [ ] Cita aparece en dashboard GHL
- [ ] Cita reprogramada exitosamente
- [ ] Cambio reflejado en dashboard GHL
- [ ] Consistencia de IDs mantenida
