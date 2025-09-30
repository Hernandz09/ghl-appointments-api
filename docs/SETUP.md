# Guía de Configuración Inicial - Backend API

## 🚀 Configuración Rápida

### 1. Clonar el Repositorio
```bash
git clone <tu-repositorio>
cd GHL_WebhooksS2
```

### 2. Configurar Variables de Entorno
**⚠️ PASO OBLIGATORIO**: Debes crear el archivo `.env` antes de continuar.

```bash
# Copiar el archivo de ejemplo
cp .env.example .env

# Editar con tus credenciales
# Usa cualquier editor: notepad, vscode, etc.
```

### 3. Instalar Dependencias
```bash
cd backend
pip install -r requirements.txt
```

### 4. Configurar Base de Datos
SQLite se configura automáticamente. Solo ejecuta las migraciones:
```bash
cd backend
python manage.py migrate
```

### 5. Iniciar Servidor
```bash
cd backend
python manage.py runserver
```

**✅ Verificación**: Deberías ver:
```
Starting development server at http://127.0.0.1:8000/
```

## 🔧 Configuración Detallada

### Variables de Entorno Requeridas

| Variable | Descripción | Ejemplo |
|----------|-------------|---------|
| `SECRET_KEY` | Clave secreta de Django | `django-insecure-...` |
| `DEBUG` | Modo debug | `True` |
| `ALLOWED_HOSTS` | Hosts permitidos | `127.0.0.1,localhost` |
| `GHL_ACCESS_TOKEN` | Token de GoHighLevel | `ghl_token_...` |
| `GHL_API_KEY` | API Key de GoHighLevel | `ghl_api_...` |
| `GHL_LOCATION_ID` | ID de ubicación GHL | `CRlTCqv7ASS9xOpPQ59O` |
| `GHL_ASSIGNED_USER_ID` | ID de usuario asignado | `lFqIyq3yCE6mZxNwIcID` |

### Estructura del Archivo .env
```env
# Django
SECRET_KEY=django-insecure-tu-secret-key-muy-largo-y-seguro
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost

# GoHighLevel
GHL_ACCESS_TOKEN=ghl_token_tu_token_aqui
GHL_API_KEY=ghl_api_tu_api_key_aqui
GHL_LOCATION_ID=CRlTCqv7ASS9xOpPQ59O
GHL_ASSIGNED_USER_ID=lFqIyq3yCE6mZxNwIcID
```

## 🐛 Solución de Problemas

### Error: "No module named 'django'"
```bash
# Activar el entorno virtual
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# Instalar dependencias
pip install -r requirements.txt
```

### Error: "Cannot connect to database"
- SQLite se crea automáticamente
- Verificar que el archivo `db.sqlite3` exista
- Ejecutar migraciones: `python manage.py migrate`

### Error: "GHL_ACCESS_TOKEN not found"
- Verificar que el archivo `.env` exista
- Asegurarse de que `GHL_ACCESS_TOKEN` esté configurado
- Reiniciar el servidor después de cambiar `.env`

### Error: "500 Internal Server Error"
- Revisar la consola de Django para ver el error específico
- Verificar que todas las variables de entorno estén configuradas
- Asegurarse de que GHL_ACCESS_TOKEN sea válido

## 📞 Soporte

Si tienes problemas con la configuración:
1. Revisa que todas las variables de entorno estén configuradas
2. Verifica que las dependencias estén instaladas
3. Asegúrate de que el servidor Django esté ejecutándose
4. Revisa los logs de error en la consola
