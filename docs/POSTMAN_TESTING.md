# 🧪 Guía de Pruebas con Postman - GHL Sala 02

## 📋 Índice
- [Instalación y Configuración](#instalación-y-configuración)
- [Conceptos Básicos](#conceptos-básicos)
- [Configuración Inicial](#configuración-inicial)
- [Pruebas de Endpoints](#pruebas-de-endpoints)
- [Flujo Completo Sala 2](#flujo-completo-sala-2)
- [Solución de Problemas](#solución-de-problemas)
- [Checklist de Verificación](#checklist-de-verificación)

## 📥 Instalación y Configuración

### 1. Descargar Postman
1. Ve a [postman.com/downloads](https://www.postman.com/downloads/)
2. Descarga la versión para Windows
3. Instala y crea una cuenta gratuita
4. Abre Postman

### 2. Verificar Servidor Django
Antes de empezar, asegúrate de que tu servidor Django esté corriendo:

```bash
cd backend
python manage.py runserver
```

**✅ Verificación:** Deberías ver en la consola:
```
Starting development server at http://127.0.0.1:8000/
```

## 🎯 Conceptos Básicos

### Métodos HTTP
- **GET**: Obtener datos (listar citas)
- **POST**: Crear nuevos datos (crear cita)
- **PUT**: Actualizar datos existentes (reprogramar cita)
- **DELETE**: Eliminar datos (cancelar cita)

### Estructura de Request
- **URL**: Dirección del endpoint
- **Headers**: Información adicional (Content-Type, etc.)
- **Body**: Datos que envías (en formato JSON)

### Códigos de Respuesta
- **200**: ✅ Éxito
- **201**: ✅ Creado exitosamente
- **400**: ❌ Error en los datos enviados
- **404**: ❌ No encontrado
- **500**: ❌ Error del servidor

## ⚙️ Configuración Inicial

### 1. Crear Nueva Request
1. En Postman, haz clic en **"New"** → **"HTTP Request"**
2. Se abrirá una nueva pestaña

### 2. Configurar Variables (Opcional pero Recomendado)
1. Haz clic en el ícono de engranaje ⚙️ (Settings)
2. Ve a **"Variables"**
3. Agrega:
   - **Variable**: `base_url`
   - **Initial Value**: `http://localhost:8000`
   - **Current Value**: `http://localhost:8000`

Ahora puedes usar `{{base_url}}` en tus URLs.

## 🔌 Pruebas de Endpoints

### 1. 📋 Listar Citas (GET)

#### Configuración:
- **Método**: `GET`
- **URL**: `{{base_url}}/api/appointments/appointments/`
- **Headers**: No necesarios

#### Pasos:
1. Selecciona **GET** en el dropdown
2. En la URL escribe: `http://localhost:8000/api/appointments/appointments/`
3. Haz clic en **"Send"**

#### Resultado Esperado:
```json
[
    {
        "id": 1,
        "ghl_id": "I2bsjgvM7rslohU9w1NJ",
        "location_id": "CRlTCqv7ASS9xOpPQ59O",
        "calendar_id": "2fgVoaRLnypQzl83H5gf",
        "contact_id": "MfGsfig9eluEgIML9Huw",
        "title": "Cita medica ( reagendada)",
        "appointment_status": "cancelled",
        "assigned_user_id": "lFqIyq3yCE6mZxNwIcID",
        "notes": null,
        "start_time": "2025-09-25T05:00:00Z",
        "end_time": "2025-09-26T05:00:00Z",
        "source": "calendar_page",
        "date_added": "2025-09-24T04:31:04.727Z",
        "date_updated": "2025-09-30T00:38:30.193Z"
    }
]
```

#### ✅ Verificación:
- **Status**: `200 OK`
- **Response**: Array con las citas existentes

---

### 2. ➕ Crear Cita (POST)

#### Configuración:
- **Método**: `POST`
- **URL**: `{{base_url}}/api/appointments/create/`
- **Headers**: 
  - `Content-Type: application/json`
- **Body**: JSON con los datos de la cita

#### Pasos:
1. Cambia el método a **POST**
2. URL: `http://localhost:8000/api/appointments/create/`
3. Ve a la pestaña **"Headers"**
4. Agrega:
   - **Key**: `Content-Type`
   - **Value**: `application/json`
5. Ve a la pestaña **"Body"**
6. Selecciona **"raw"** y **"JSON"**
7. Copia y pega este JSON:

```json
{
    "calendarId": "2fgVoaRLnypQzl83H5gf",
    "contactId": "MfGsfig9eluEgIML9Huw",
    "startTime": "2025-10-02T10:00:00Z",
    "endTime": "2025-10-02T11:00:00Z",
    "title": "Cita de prueba desde Postman",
    "locationId": "CRlTCqv7ASS9xOpPQ59O",
    "assignedUserId": "lFqIyq3yCE6mZxNwIcID",
    "appointmentStatus": "confirmed"
}
```

8. Haz clic en **"Send"**

#### Resultado Esperado:
```json
{
    "id": 2,
    "ghl_id": "nuevo_id_generado_por_ghl",
    "location_id": "CRlTCqv7ASS9xOpPQ59O",
    "calendar_id": "2fgVoaRLnypQzl83H5gf",
    "contact_id": "MfGsfig9eluEgIML9Huw",
    "title": "Cita de prueba desde Postman",
    "appointment_status": "confirmed",
    "assigned_user_id": "lFqIyq3yCE6mZxNwIcID",
    "notes": null,
    "start_time": "2025-10-02T10:00:00Z",
    "end_time": "2025-10-02T11:00:00Z",
    "source": null,
    "date_added": "2025-01-15T10:30:00Z",
    "date_updated": "2025-01-15T10:30:00Z"
}
```

#### ✅ Verificación:
- **Status**: `201 Created`
- **Response**: Objeto con la cita creada
- **ghl_id**: Debe tener un valor generado por GHL

---

### 3. ✏️ Actualizar/Reprogramar Cita (PUT)

#### Configuración:
- **Método**: `PUT`
- **URL**: `{{base_url}}/api/appointments/update/{ghl_id}/`
- **Headers**: 
  - `Content-Type: application/json`
- **Body**: JSON con los campos a actualizar

#### Pasos:
1. Cambia el método a **PUT**
2. URL: `http://localhost:8000/api/appointments/update/I2bsjgvM7rslohU9w1NJ/`
   - ⚠️ **Importante**: Reemplaza `I2bsjgvM7rslohU9w1NJ` con el `ghl_id` real de tu cita
3. Headers: `Content-Type: application/json`
4. Body (raw JSON):

```json
{
    "startTime": "2025-10-03T14:00:00Z",
    "endTime": "2025-10-03T15:00:00Z",
    "title": "Cita reprogramada desde Postman",
    "appointmentStatus": "confirmed"
}
```

5. Haz clic en **"Send"**

#### Resultado Esperado:
```json
{
    "startTime": "2025-10-03T14:00:00Z",
    "endTime": "2025-10-03T15:00:00Z",
    "title": "Cita reprogramada desde Postman",
    "appointmentStatus": "confirmed"
}
```

#### ✅ Verificación:
- **Status**: `200 OK`
- **Response**: Datos actualizados
- **Consistencia**: El `ghl_id` debe mantenerse igual

---

### 4. 🗑️ Cancelar Cita (DELETE)

#### Configuración:
- **Método**: `DELETE`
- **URL**: `{{base_url}}/api/appointments/delete/{ghl_id}/`
- **Headers**: No necesarios

#### Pasos:
1. Cambia el método a **DELETE**
2. URL: `http://localhost:8000/api/appointments/delete/I2bsjgvM7rslohU9w1NJ/`
3. Haz clic en **"Send"**

#### Resultado Esperado:
```json
{
    "message": "Cita cancelada correctamente"
}
```

#### ✅ Verificación:
- **Status**: `200 OK`
- **Response**: Mensaje de confirmación

---

## 🟩 Flujo Completo Sala 2

### Objetivo: Crear cita para mañana → Reprogramar para pasado mañana → Verificar en GHL

### Paso 1: Crear Cita para Mañana

**Request:**
```json
POST http://localhost:8000/api/appointments/create/
{
    "calendarId": "2fgVoaRLnypQzl83H5gf",
    "contactId": "MfGsfig9eluEgIML9Huw",
    "startTime": "2025-10-02T10:00:00Z",
    "endTime": "2025-10-02T11:00:00Z",
    "title": "Cita para mañana - Sala 2",
    "locationId": "CRlTCqv7ASS9xOpPQ59O",
    "assignedUserId": "lFqIyq3yCE6mZxNwIcID",
    "appointmentStatus": "confirmed"
}
```

**Resultado Esperado:**
```json
{
    "id": 3,
    "ghl_id": "ABC123DEF456",
    "title": "Cita para mañana - Sala 2",
    "start_time": "2025-10-02T10:00:00Z",
    "end_time": "2025-10-02T11:00:00Z",
    "appointment_status": "confirmed"
}
```

**✅ Verificación:**
- Anota el `ghl_id` de la respuesta (ej: `ABC123DEF456`)
- Verifica que la cita aparece en el dashboard de GHL ReflexoPerú

### Paso 2: Reprogramar para Pasado Mañana

**Request:**
```json
PUT http://localhost:8000/api/appointments/update/ABC123DEF456/
{
    "startTime": "2025-10-03T14:00:00Z",
    "endTime": "2025-10-03T15:00:00Z",
    "title": "Cita reprogramada para pasado mañana - Sala 2"
}
```

**Resultado Esperado:**
```json
{
    "startTime": "2025-10-03T14:00:00Z",
    "endTime": "2025-10-03T15:00:00Z",
    "title": "Cita reprogramada para pasado mañana - Sala 2"
}
```

**✅ Verificación:**
- **Status**: `200 OK`
- **Consistencia**: El `ghl_id` se mantiene igual (`ABC123DEF456`)
- **Cambio reflejado**: La nueva fecha/hora aparece en GHL

### Paso 3: Verificar Cambio en GHL

1. **En Postman**: Haz un GET para verificar los datos locales
2. **En GHL Dashboard**: Verifica que la cita aparece con la nueva fecha/hora
3. **Consistencia**: Confirma que el ID original se mantiene

---

## 🚨 Solución de Problemas

### Error: "Connection refused"
**Causa**: Servidor Django no está corriendo
**Solución**:
```bash
cd backend
python manage.py runserver
```

### Error: "404 Not Found"
**Causa**: URL incorrecta o endpoint no existe
**Solución**:
- Verifica que la URL sea correcta
- Asegúrate de que el endpoint exista en `urls.py`

### Error: "400 Bad Request"
**Causa**: JSON mal formateado o campos faltantes
**Solución**:
- Verifica que el JSON esté bien formateado
- Asegúrate de incluir todos los campos requeridos
- Revisa que `Content-Type: application/json` esté en headers

### Error: "500 Internal Server Error"
**Causa**: Error en el servidor
**Solución**:
- Revisa la consola de Django para ver el error específico
- Verifica que las variables de entorno estén configuradas
- Asegúrate de que GHL_ACCESS_TOKEN esté configurado

### Error: "NOT NULL constraint failed"
**Causa**: Campo requerido está llegando como null
**Solución**:
- Verifica que todos los campos requeridos estén en el JSON
- Asegúrate de que los valores no sean null

---

## 📊 Checklist de Verificación

### ✅ Configuración Inicial
- [ ] Postman instalado y funcionando
- [ ] Servidor Django corriendo en puerto 8000
- [ ] Variables de entorno configuradas (.env)
- [ ] GHL_ACCESS_TOKEN configurado

### ✅ Endpoints Básicos
- [ ] GET /api/appointments/appointments/ → Lista citas
- [ ] POST /api/appointments/create/ → Crea cita
- [ ] PUT /api/appointments/update/{id}/ → Actualiza cita
- [ ] DELETE /api/appointments/delete/{id}/ → Cancela cita

### ✅ Flujo Sala 2
- [ ] Crear cita para mañana → Éxito
- [ ] Reprogramar para pasado mañana → Éxito
- [ ] Verificar cambio en GHL dashboard → Visible
- [ ] Consistencia de ID original → Mantenido

### ✅ Validaciones
- [ ] Códigos de respuesta correctos (200, 201)
- [ ] JSON bien formateado en respuestas
- [ ] Campos requeridos presentes
- [ ] Manejo de errores funcionando

---

## 📝 Notas Importantes

### Campos Requeridos para Crear Cita
- `calendarId`: ID del calendario en GHL
- `contactId`: ID del contacto en GHL
- `startTime`: Fecha/hora de inicio (ISO 8601)
- `endTime`: Fecha/hora de fin (ISO 8601)
- `locationId`: ID de la ubicación en GHL
- `assignedUserId`: ID del usuario asignado

### Formato de Fechas
- **Formato**: ISO 8601 con timezone UTC
- **Ejemplo**: `2025-10-02T10:00:00Z`
- **Z**: Indica timezone UTC

### IDs de GHL
- **ghl_id**: ID único generado por GoHighLevel
- **Formato**: String alfanumérico
- **Ejemplo**: `I2bsjgvM7rslohU9w1NJ`

---

## 🎯 Resultados Esperados

### ✅ Éxito Completo
- Todos los endpoints funcionan correctamente
- Citas se crean y actualizan en GHL
- Cambios se reflejan en el dashboard de ReflexoPerú
- Consistencia de IDs mantenida
- Manejo de errores robusto

### 📊 Métricas de Éxito
- **Tiempo de respuesta**: < 2 segundos
- **Tasa de éxito**: 100% en operaciones válidas
- **Sincronización**: Inmediata con GHL
- **Consistencia**: 100% en IDs

---

**🏥 GHL Sala 02 - Sistema de Citas**  
*Documentación de pruebas con Postman*

**Última actualización**: Enero 2025
