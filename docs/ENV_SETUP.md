# 🔐 Configuración de Variables de Entorno - Backend API

## ⚠️ IMPORTANTE: Debes crear el archivo .env

**El archivo `.env` NO se incluye en el repositorio por seguridad.**

### Pasos para configurar:

1. **Copia el archivo de ejemplo:**
   ```bash
   cp .env.example .env
   ```

2. **Edita el archivo `.env` con tus credenciales:**
   ```bash
   # Usa cualquier editor
   notepad .env
   # o
   code .env
   ```

3. **Reemplaza los valores de ejemplo con tus datos reales:**

### Variables Requeridas:

#### 🗄️ Base de Datos SQLite
```env
# SQLite se configura automáticamente
# No se requieren variables de entorno para SQLite
# La base de datos se crea en: backend/db.sqlite3
```

#### 🐍 Django
```env
SECRET_KEY=django-insecure-tu-secret-key-muy-largo-y-seguro
DEBUG=True                     # False en producción
ALLOWED_HOSTS=127.0.0.1,localhost
```

#### 🔗 GoHighLevel API
```env
GHL_ACCESS_TOKEN=ghl_token_tu_token_aqui
GHL_API_KEY=ghl_api_tu_api_key_aqui
GHL_LOCATION_ID=CRlTCqv7ASS9xOpPQ59O
GHL_ASSIGNED_USER_ID=lFqIyq3yCE6mZxNwIcID
```

### Ejemplo de archivo .env completo:
```env
# Django
SECRET_KEY=django-insecure-abc123def456ghi789jkl012mno345pqr678stu901vwx234yz
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost

# GoHighLevel
GHL_ACCESS_TOKEN=ghl_token_abc123def456
GHL_API_KEY=ghl_api_xyz789uvw456
GHL_LOCATION_ID=CRlTCqv7ASS9xOpPQ59O
GHL_ASSIGNED_USER_ID=lFqIyq3yCE6mZxNwIcID
```

### 🚨 Seguridad:
- **NUNCA** subas el archivo `.env` a Git
- **NUNCA** compartas tus credenciales
- Usa contraseñas seguras
- En producción, usa `DEBUG=False`

### ✅ Verificación:
Después de crear el archivo `.env`, puedes verificar que funciona ejecutando:
```bash
cd backend
python manage.py check
```

Si no hay errores, la configuración es correcta.
