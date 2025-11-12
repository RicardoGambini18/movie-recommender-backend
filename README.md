# Algolab - Backend API

Algolab es un laboratorio interactivo de algoritmos y estructuras de datos que permite experimentar con distintas implementaciones, comparar su rendimiento y visualizar su comportamiento en tiempo real, incluyendo comparadores de algoritmos de búsqueda y ordenamiento.

> **⚠️ Nota Importante:** El proceso de configuración local puede resultar complejo. Si no se necesita ejecutar la aplicación localmente, se puede utilizar las versiones desplegadas:
>
> - **Backend API:** Disponible en **https://algolab-backend.vercel.app/apidocs**
> - **Frontend:** Interfaz web optimizada y fácil de usar que consume esta API. Aunque no es parte directa de este proyecto, se desarrolló con la finalidad de facilitar el uso de la aplicación. Disponible en **https://algolab-frontend.vercel.app**
>   - **Nota de acceso:** Al ingresar, se requiere un proceso de login donde se debe seleccionar un usuario cualquiera y colocar la contraseña: **33396** (sección del curso).

## 📋 Requerimientos del Sistema

- **Python**: 3.11 o superior
- **PostgreSQL**: 13 o superior

## 🚀 Instalación y Configuración

### 1. Extraer el Proyecto
Extraer el archivo ZIP del proyecto y navegar a la carpeta:
```bash
cd algolab-backend
```

### 2. Crear Entorno Virtual
```bash
python -m venv .venv
```

### 3. Activar Entorno Virtual

**Windows:**
```bash
.venv\Scripts\activate
```

**macOS/Linux:**
```bash
source .venv/bin/activate
```

### 4. Instalar Dependencias
```bash
pip install -r requirements.txt
```

### 5. Configurar Variables de Entorno

Crear archivo `.env` en la raíz del proyecto con las siguientes variables:

```env
# Base de datos (REQUERIDA)
DATABASE_URL=postgresql://usuario:password@localhost:5432/algolab

# Configuración de Flask (opcionales)
FLASK_ENV=development
FLASK_DEBUG=1
FLASK_RUN_PORT=8080

# Límites de datos (opcionales)
# * Ajustar dependiendo de las capacidades de la computadora donde se ejecutará la App
MOVIES_SORT_LIMIT=10000
WARMUP_ITERATIONS=25000

# TMDB API (opcional - solo para actualización de datos)
TMDB_API_KEY=tu_api_key_aqui
```

#### 🔑 Cómo Obtener la API Key de TMDB

La API Key de TMDB es necesaria solo para el comando `flask data:update`. Para obtenerla:

1. **Crear cuenta en TMDB:**
   - Visitar: https://www.themoviedb.org/signup
   - Completar el registro con email y contraseña

2. **Solicitar API Key:**
   - Ir a: https://www.themoviedb.org/settings/api
   - Hacer clic en "Request an API Key"
   - Seleccionar "Developer" como tipo de uso
   - Completar el formulario. Además de los campos personales requeridos, completar los siguientes campos relacionados con la aplicación:
     - **Application Name**: Algolab Backend
     - **Application Summary**: Proyecto académico para curso de algoritmos y estructuras de datos
     - **Application URL**: http://localhost:8080 (o tu URL de desarrollo)

3. **Obtener la Key:**
   - Una vez aprobada, copiar la "API Key (v3 auth)"
   - Agregarla al archivo `.env` como: `TMDB_API_KEY=tu_api_key_aqui`

**⚠️ Nota:** El proceso de aprobación puede tomar unos minutos. La API Key es gratuita para uso académico y personal.

### 6. Configurar Base de Datos

**Crear base de datos en PostgreSQL:**
```sql
CREATE DATABASE algolab;
```

**Aplicar migraciones:**
```bash
flask db upgrade
```

## 📊 Carga de Datos

### Paso 1: Descargar Dataset
```bash
flask data:download
```
Descarga los archivos CSV de The Movies Dataset desde una carpeta pública en Google Drive a la carpeta `data/`. Este comando limpia la carpeta antes de descargar.

### Paso 2: Migrar Datos a Base de Datos
```bash
flask seed
```
Formatea los datos de los archivos CSV y los ingresa a la base de datos. **⚠️ Este comando elimina todos los datos existentes.**

### Paso 3: Actualizar Datos (Opcional)
```bash
flask data:update
```
Accede a la API de TMDB para actualizar información de películas y agregar campos en español. **⚠️ Requiere `TMDB_API_KEY` y puede tardar varias horas.**

## 🏃‍♂️ Ejecutar la Aplicación

```bash
flask run
```

La aplicación estará disponible en:
- **URL**: http://localhost:8080
- **Documentación API**: http://localhost:8080/apidocs

## 📚 Comandos Disponibles

### Comandos de Base de Datos
```bash
# Inicializar migraciones (solo primera vez)
flask db init

# Crear nueva migración
flask db migrate -m "descripción de la migración"

# Aplicar migraciones pendientes
flask db upgrade

# Revertir última migración
flask db downgrade
```

### Comandos de Datos
```bash
# Descargar dataset de películas
flask data:download

# Migrar datos CSV a base de datos
flask seed

# Actualizar datos desde TMDB API
flask data:update
```

### Comando de Desarrollo
```bash
# Iniciar servidor de desarrollo
flask run
```

## 📖 Documentación de la API

Una vez que la aplicación esté ejecutándose, puedes acceder a la documentación interactiva de Swagger en:
- **URL**: http://localhost:8080/apidocs

### 🔍 Endpoints Principales

- `GET /api/movies/sort/data-structures` - Obtener algoritmos de ordenamiento disponibles
- `GET /api/movies/sort` - Ejecutar algoritmo de ordenamiento
- `GET /api/movies/search/data-structures` - Obtener algoritmos de búsqueda disponibles
- `GET /api/movies/search` - Ejecutar algoritmo de búsqueda
- `GET /api/movies` - Obtener todas las películas
- `GET /api/users` - Obtener todos los usuarios

### 📋 Guía de Uso de Swagger

**Swagger** es una interfaz interactiva que permite probar todos los endpoints directamente desde el navegador:

1. **Acceder a Swagger:**
   - Abrir http://localhost:8080/apidocs en el navegador
   - Verás la documentación completa de todos los endpoints

2. **Probar Endpoints de Algoritmos:**
   - **Obtener algoritmos disponibles:**
     - Expandir `GET /api/movies/sort/data-structures`
     - Hacer clic en "Try it out" → "Execute"
     - Verás la lista de algoritmos de ordenamiento disponibles
   
   - **Ejecutar algoritmo de ordenamiento:**
     - Expandir `GET /api/movies/sort`
     - Hacer clic en "Try it out"
     - Ingresar parámetros:
       - `algorithm_key`: `bubble_sort` (o cualquier algoritmo disponible)
       - `data_structure_key`: `vector`
     - Hacer clic en "Execute"
     - Verás el resultado con métricas de rendimiento

3. **Probar Endpoints de Búsqueda:**
   - **Obtener algoritmos de búsqueda:**
     - Expandir `GET /api/movies/search/data-structures`
     - Hacer clic en "Try it out" → "Execute"
   
   - **Ejecutar algoritmo de búsqueda:**
     - Expandir `GET /api/movies/search`
     - Hacer clic en "Try it out"
     - Ingresar parámetros:
       - `movie_id`: `1` (ID de película a buscar)
       - `algorithm_key`: `linear_search` (o cualquier algoritmo disponible)
       - `data_structure_key`: `vector`
     - Hacer clic en "Execute"

4. **Ver Datos:**
   - **Obtener películas:** `GET /api/movies` → "Try it out" → "Execute"
   - **Obtener usuarios:** `GET /api/users` → "Try it out" → "Execute"

**💡 Tip:** Cada respuesta incluye métricas detalladas como número de comparaciones, tiempo de ejecución y complejidad del algoritmo.

## ⚠️ Notas Importantes

1. **Primera ejecución**: Siempre ejecutar `flask db upgrade` antes de `flask seed`
2. **Comando `seed`**: Elimina todos los datos existentes antes de insertar nuevos
3. **Comando `data:update`**: Requiere API key de TMDB y puede tardar horas
4. **Puerto por defecto**: 8080 (configurable con `FLASK_RUN_PORT`)
5. **Núcleo académico**: Los algoritmos están en la carpeta `core/` sin dependencias externas
