# Algolab - Python Server

Algolab es un laboratorio interactivo enfocado en comparar algoritmos de búsqueda y ordenamiento, midiendo tiempo de ejecución, uso de memoria, número de operaciones y número de iteraciones para cada implementación disponible. Esta es la versión Python del servidor.

## 🎯 Configuración Local Automática

Para facilitar la ejecución del proyecto, se ha implementado una **configuración automática simplificada** que elimina la necesidad de realizar pasos manuales de instalación y configuración.

Se ha creado un script de inicialización automática (`app.py`) que realiza todas las tareas de configuración de forma transparente. Simplemente ejecute el archivo `app.py` y el script se encargará automáticamente de:

1. **Crear y activar el entorno virtual** (si no existe) en la carpeta `.venv/`
2. **Crear el archivo `.env`** copiando automáticamente `.env.example` cuando sea necesario
3. **Descargar la base de datos SQLite `algolab.db`** desde Google Drive y colocarla en la carpeta `instance/`. Este archivo también puede generarse manualmente con el repositorio [`tmdb-db-generator`](https://github.com/RicardoGambini18/tmdb-db-generator) y debe ubicarse en `instance/algolab.db`
4. **Descargar y descomprimir el build del frontend** desde Google Drive (`frontend.zip`). Si se desea generar manualmente, se puede compilar el proyecto [`algolab-web-client`](https://github.com/RicardoGambini18/algolab-web-client)
5. **Instalar todas las dependencias** necesarias desde `requirements.txt`
6. **Iniciar el servidor Flask**
7. **Abrir la aplicación en el navegador** automáticamente una vez que el servidor esté listo, cargando la interfaz web de la carpeta `frontend/` para que se pueda utilizar la aplicación completa de forma local sin pasos adicionales

Al abrir la interfaz local, se debe seleccionar cualquier usuario disponible e ingresar la sección del curso (**33396**) como contraseña para iniciar sesión y comenzar a probar la aplicación.

**Nota:** La primera ejecución puede tardar unos minutos mientras se crea el entorno virtual, se copian las variables de entorno y se descargan los recursos. Las ejecuciones posteriores serán más rápidas porque reutilizan todo lo configurado localmente. Si se desea usar otra base de datos, basta con editar el `.env` generado después de la primera ejecución.

> **⚠️ Nota Importante:** Si no se necesita ejecutar la aplicación localmente, se puede utilizar la versión desplegada en **https://algolab-aed.vercel.app**.

## 📊 Métricas Registradas

Cada ejecución de un algoritmo reporta las siguientes métricas para facilitar el análisis comparativo:

- **Tiempo (ns):** Duración total medida con `time.perf_counter_ns`.
- **Memoria (bytes):** Diferencia entre el pico y el uso inicial registrado con `tracemalloc`.
- **Operaciones:** Conteo acumulado de comparaciones, asignaciones y operaciones matemáticas relevantes dentro del algoritmo.
- **Iteraciones:** Total de ciclos ejecutados en bucles y llamadas recursivas, útil para dimensionar el esfuerzo estructural del algoritmo.

## 📋 Requerimientos del Sistema

- **Python**: 3.11 o superior
- **PostgreSQL**: 13 o superior

## 🚀 Instalación y Configuración

### 1. Navegar al Proyecto
Clonar el repositorio o descargarlo y luego ingresar a la carpeta:
```bash
cd algolab-python-server
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
# Para PostgreSQL:
DATABASE_URI=postgresql://usuario:password@localhost:5432/algolab
# Para SQLite (la base de datos debe estar en instance/algolab.db):
# DATABASE_URI=sqlite+pysqlite:///algolab.db

# Configuración de Flask (opcionales)
FLASK_DEBUG=1
FLASK_RUN_PORT=8080

# Límites de datos (opcionales)
# * Ajustar dependiendo de las capacidades de la computadora donde se ejecutará la App
MOVIES_SORT_LIMIT=10000
WARMUP_ITERATIONS=25000
```

### 6. Configurar Base de Datos

Este proyecto asume que ya cuentas con una base de datos generada mediante [`tmdb-db-generator`](https://github.com/RicardoGambini18/tmdb-db-generator), que soporta tanto PostgreSQL como SQLite. Una vez creada, configura `DATABASE_URI` en el archivo `.env` para apuntar a esa instancia:

- **Para PostgreSQL:** Usa una URI como `postgresql://usuario:password@localhost:5432/algolab`. La base de datos debe estar corriendo en tu servidor PostgreSQL.
- **Para SQLite:** Usa una URI relativa como `sqlite+pysqlite:///algolab.db`. La base de datos debe estar ubicada en la carpeta `instance/` con el nombre `algolab.db` (es decir, `instance/algolab.db`). La carpeta `instance/` es creada automáticamente por Flask y es donde se almacenan archivos específicos de la instancia de la aplicación.

### 7. (Opcional) Compilar Frontend local

Si deseas servir la interfaz de usuario localmente, puedes compilar el proyecto [`algolab-web-client`](https://github.com/RicardoGambini18/algolab-web-client) (Next.js) siguiendo las instrucciones de su propio README. Una vez generado el build estático, copia los archivos resultantes a la carpeta `frontend/` en este repositorio. Al iniciar el servidor Flask, los archivos se servirán automáticamente.

## 🏃‍♂️ Ejecutar la Aplicación

```bash
flask run
```

Una vez levantado el servidor podrás acceder a la documentación Swagger en http://localhost:${FLASK_RUN_PORT}/apidocs. Si la carpeta `frontend/` está presente, la raíz http://localhost:${FLASK_RUN_PORT}/ mostrará la UI (login + dashboard); de lo contrario solo se expondrán los endpoints de la API.

### 🖥️ Guía rápida de la interfaz web

Si la carpeta `frontend/` está presente, al abrir http://localhost:${FLASK_RUN_PORT}/ verás la pantalla de login:

1. Selecciona cualquier usuario.
2. Ingresa como contraseña el valor de la variable `AUTH_PASSWORD`.
3. Hacer click en “Iniciar Sesión”. Serás redirigido al dashboard con los módulos de algoritmos de búsqueda y ordenamiento.
4. Cada módulo describe los pasos para ejecutar pruebas; basta con elegir los parámetros y ejecutar para ver métricas y resultados.

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
   - Abrir http://localhost:${FLASK_RUN_PORT}/apidocs en el navegador
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
