# Algolab - Backend API

Algolab es un laboratorio interactivo enfocado en comparar algoritmos de búsqueda y ordenamiento, midiendo tiempo de ejecución, uso de memoria y número de comparaciones para cada implementación disponible.

## 🎯 Configuración Local Automática

Para facilitar la ejecución del proyecto, se ha implementado una **configuración automática simplificada** que elimina la necesidad de realizar pasos manuales de instalación y configuración.

Se ha creado un script de inicialización automática (`app.py`) que realiza todas las tareas de configuración de forma transparente. Simplemente ejecute el archivo `app.py` y el script se encargará automáticamente de:

1. **Crear y activar el entorno virtual** (si no existe) en la carpeta `.venv/`
2. **Instalar todas las dependencias** necesarias desde `requirements.txt`
3. **Iniciar el servidor Flask**
4. **Abrir la aplicación en el navegador** automáticamente una vez que el servidor esté listo, cargando la interfaz web de la carpeta `frontend/` para que se pueda utilizar la aplicación completa de forma local sin pasos adicionales

Al abrir la interfaz local, se debe seleccionar cualquier usuario disponible e ingresar la sección del curso (**33396**) como contraseña para iniciar sesión y comenzar a probar la aplicación.

**Nota:** La primera ejecución puede tardar unos minutos mientras se crea el entorno virtual e instalan las dependencias. Las ejecuciones posteriores serán más rápidas ya que reutilizará el entorno virtual existente. El archivo `.env` proporcionado incluye configuración de base de datos en la nube, por lo que no es necesario configurar PostgreSQL localmente.

> **⚠️ Nota Importante:** Si no se necesita ejecutar la aplicación localmente, se puede utilizar la versión desplegada en **https://algolab-utp.vercel.app**.

## 📋 Requerimientos del Sistema

- **Python**: 3.11 o superior
- **PostgreSQL**: 13 o superior

## 🚀 Instalación y Configuración

### 1. Navegar al Proyecto
Clonar el repositorio o descargarlo y luego ingresar a la carpeta:
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
```

### 6. Configurar Base de Datos

Este proyecto asume que ya cuentas con una base de datos generada mediante [`tmdb-db-generator`](https://github.com/RicardoGambini18/tmdb-db-generator). Una vez creada, solo necesitas configurar `DATABASE_URL` para apuntar a esa instancia. No se requiere ejecutar migraciones ni comandos adicionales en este repositorio; basta con reutilizar la base provista.

## 🏃‍♂️ Ejecutar la Aplicación

```bash
flask run
```

Una vez levantado el servidor podrás acceder a la app en http://localhost:8080 y a la documentación Swagger en http://localhost:8080/apidocs.

### 🔍 Endpoints Disponibles

- `GET /api/movies/sort/data-structures` - Obtener algoritmos de ordenamiento disponibles
- `GET /api/movies/sort` - Ejecutar algoritmo de ordenamiento
- `GET /api/movies/search/data-structures` - Obtener algoritmos de búsqueda disponibles
- `GET /api/movies/search` - Ejecutar algoritmo de búsqueda
- `GET /api/movies` - Obtener todas las películas
- `GET /api/users` - Obtener todos los usuarios
- `POST /api/users/login` - Iniciar sesión y obtener un token JWT

### 📋 Guía de Uso de Swagger

**Swagger** es una interfaz interactiva que permite probar todos los endpoints directamente desde el navegador:

1. **Acceder a Swagger:**
   - Abrir http://localhost:8080/apidocs en el navegador
   - Verás la documentación completa de todos los endpoints

2. **Obtener token de acceso:**
   - Expandir `POST /api/users/login`
   - Enviar un JSON como el siguiente:
     ```json
     {
       "password": "<valor de AUTH_PASSWORD>",
       "user_id": 1
     }
     ```
   - Hacer clic en "Try it out"
   - El endpoint responderá con un token JWT para el usuario elegido

3. **Autenticación en Swagger:**
   - En la barra superior haz clic en el botón **Authorize**
   - Se abrirá un modal que solicita la `api_key`; ingresa el token con el formato `Bearer <token>`, donde `<token>` es el valor devuelto por `POST /api/users/login`
   - Pulsa nuevamente **Authorize** dentro del modal y luego **Close**
   - Las rutas de `movies` quedarán habilitadas; los endpoints de `users` no requieren token

4. **Probar Endpoints de Algoritmos:**
   - **Obtener algoritmos disponibles:**
     - Expandir `GET /api/movies/sort/data-structures`
     - Hacer clic en "Try it out"
     - Verás la lista de algoritmos de ordenamiento disponibles
   
   - **Ejecutar algoritmo de ordenamiento:**
     - Expandir `GET /api/movies/sort`
     - Ingresar parámetros:
       - `algorithm_key`: `bubble_sort` (o cualquier algoritmo disponible)
       - `data_structure_key`: `vector`
     - Hacer clic en "Try it out"
     - Verás el resultado con métricas de rendimiento

5. **Probar Endpoints de Búsqueda:**
   - **Obtener algoritmos de búsqueda:**
     - Expandir `GET /api/movies/search/data-structures`
     - Hacer clic en "Try it out"
   
   - **Ejecutar algoritmo de búsqueda:**
     - Expandir `GET /api/movies/search`
     - Ingresar parámetros:
       - `movie_id`: `1` (ID de película a buscar)
       - `algorithm_key`: `linear_search` (o cualquier algoritmo disponible)
       - `data_structure_key`: `vector`
     - Hacer clic en "Try it out"

6. **Ver Datos:**
   - **Obtener películas:** `GET /api/movies` → "Try it out"
   - **Obtener usuarios:** `GET /api/users` → "Try it out"
