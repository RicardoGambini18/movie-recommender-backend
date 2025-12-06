import os
import sys
import time
import shutil
import zipfile
import threading
import webbrowser
import subprocess
from pathlib import Path
from config.logger import Logger

script_dir = Path(__file__).parent.absolute()

if str(script_dir) not in sys.path:
    sys.path.insert(0, str(script_dir))

os.chdir(script_dir)


def ensure_venv():
    Logger.info("Verificando entorno virtual")

    in_venv = hasattr(sys, 'real_prefix') or (
        hasattr(sys, 'base_prefix') and sys.prefix != sys.base_prefix
    )

    if in_venv:
        Logger.success("Entorno virtual activo")
        return True

    venv_path = script_dir / ".venv"
    venv_python = venv_path / "bin" / "python"

    script_path = script_dir / "app.py"

    if venv_path.exists() and venv_python.exists():
        Logger.info("Re-ejecutando script dentro del entorno virtual existente")
        try:
            os.execv(str(venv_python), [str(venv_python),
                                        str(script_path)] + sys.argv[1:])
        except OSError as e:
            Logger.error(
                f"Error al re-ejecutar script en el entorno virtual: {e}")
            return False

    Logger.info("Creando entorno virtual")

    try:
        subprocess.run(
            [sys.executable, "-m", "venv", str(venv_path)],
            check=True,
            capture_output=True,
            text=True
        )
        Logger.success("Entorno virtual creado correctamente")
        Logger.info("Re-ejecutando script dentro del nuevo entorno virtual")
        try:
            os.execv(str(venv_python), [str(venv_python),
                                        str(script_path)] + sys.argv[1:])
        except OSError as e:
            Logger.error(
                f"Error al re-ejecutar script en el entorno virtual: {e}")
            return False
    except subprocess.CalledProcessError as e:
        Logger.error(f"Error al crear entorno virtual: {e.stderr}")
        return False
    except Exception as e:
        Logger.error(f"Error al crear entorno virtual: {e}")
        return False


def install_dependencies():
    Logger.info("Instalando dependencias")
    try:
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "--quiet",
                "-r", str(script_dir / "requirements.txt")],
            check=True,
            capture_output=True,
            text=True
        )
        Logger.success("Dependencias instaladas correctamente")
        return True
    except subprocess.CalledProcessError as e:
        Logger.error(f"Error al instalar dependencias: {e.stderr}")
        return False
    except Exception as e:
        Logger.error(f"Error al instalar dependencias: {e}")
        return False


ENV_FILE = script_dir / ".env"
ENV_EXAMPLE_FILE = script_dir / ".env.example"


def ensure_env_file():
    Logger.info("Verificando archivo .env")

    if ENV_FILE.exists():
        Logger.success("Archivo .env encontrado")
        return True

    try:
        shutil.copyfile(ENV_EXAMPLE_FILE, ENV_FILE)
        Logger.success("Archivo .env creado desde .env.example correctamente")
        return True
    except Exception as e:
        Logger.error(f"No se pudo crear archivo .env: {e}")
        return False


def download_from_google_drive(file_id, destination, file_name):
    import gdown

    try:
        Logger.info(f"Descargando {file_name} desde Google Drive...")
        gdown.download(id=file_id, output=str(destination), quiet=True)
        Logger.success(f"{file_name} descargado correctamente")
        return True
    except Exception as e:
        Logger.error(f"Error al descargar {file_name}: {e}")
        return False


SQLITE_DB_FILE_NAME = "algolab.db"
INSTANCE_DIR = script_dir / "instance"
SQLITE_DB_PATH = INSTANCE_DIR / SQLITE_DB_FILE_NAME


def ensure_sqlite_db():
    from config.environment import Environment

    Logger.info("Verificando base de datos SQLite")

    if not INSTANCE_DIR.exists():
        INSTANCE_DIR.mkdir(parents=True, exist_ok=True)

    if SQLITE_DB_PATH.exists():
        Logger.success("Base de datos SQLite encontrada")
        return True

    if not Environment.SQLITE_DB_GOOGLE_DRIVE_ID():
        Logger.error(
            "La variable de entorno SQLITE_DB_GOOGLE_DRIVE_ID no está definida")
        return False

    return download_from_google_drive(Environment.SQLITE_DB_GOOGLE_DRIVE_ID(), SQLITE_DB_PATH, SQLITE_DB_FILE_NAME)


def unzip_file(zip_file_path, zip_file_name, destination_path):
    try:
        Logger.info(f"Descomprimiendo archivo {zip_file_name}")

        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(destination_path)

        if zip_file_path.exists():
            zip_file_path.unlink()

        Logger.success(f"Archivo {zip_file_name} descomprimido correctamente")
        return True
    except Exception as e:
        Logger.error(f"Error al descomprimir {zip_file_name}: {e}")
        return False


FRONTEND_DIR_NAME = "frontend"
FRONTEND_PATH = script_dir / FRONTEND_DIR_NAME
FRONTEND_INDEX_FILE_NAME = "index.html"
FRONTEND_INDEX_PATH = FRONTEND_PATH / FRONTEND_INDEX_FILE_NAME
FRONTEND_ZIP_FILE_NAME = "frontend.zip"
FRONTEND_ZIP_PATH = script_dir / FRONTEND_ZIP_FILE_NAME


def ensure_frontend_assets():
    from config.environment import Environment

    Logger.info("Verificando archivos estáticos del frontend")

    if FRONTEND_INDEX_PATH.exists():
        Logger.success("Archivos estáticos del frontend encontrados")
        return True

    Logger.info("No se encontraron archivos estáticos del frontend válidos")
    Logger.info("Descargando archivos estáticos del frontend")

    if not Environment.FRONTEND_ZIP_GOOGLE_DRIVE_ID():
        Logger.error(
            "La variable de entorno FRONTEND_ZIP_GOOGLE_DRIVE_ID no está definida")
        return False

    if FRONTEND_PATH.exists():
        Logger.info("Eliminando carpeta frontend")
        shutil.rmtree(FRONTEND_PATH)

    if FRONTEND_ZIP_PATH.exists():
        Logger.info("Eliminando archivo frontend.zip")
        FRONTEND_ZIP_PATH.unlink()

    if not download_from_google_drive(Environment.FRONTEND_ZIP_GOOGLE_DRIVE_ID(), FRONTEND_ZIP_PATH, FRONTEND_ZIP_FILE_NAME):
        return False

    return unzip_file(FRONTEND_ZIP_PATH, FRONTEND_ZIP_FILE_NAME, script_dir)


def open_browser(port):
    time.sleep(1.5)
    url = f"http://localhost:{port}"
    Logger.info(f"Abriendo aplicación en el navegador")
    webbrowser.open(url)


def run_server():
    from server import app
    from config.constants import port, mode, debug

    browser_thread = threading.Thread(
        target=open_browser, args=(port,), daemon=True)
    browser_thread.start()

    Logger.success(
        f"Servidor iniciado correctamente en modo {mode}. Disponible en http://localhost:{port}")

    app.run(debug=debug, port=port)


def main():
    Logger.info("Iniciando Algolab")
    Logger.info("Validando configuración")

    if not ensure_venv():
        sys.exit(1)

    if not install_dependencies():
        sys.exit(1)

    if not ensure_env_file():
        sys.exit(1)

    if not ensure_sqlite_db():
        sys.exit(1)

    if not ensure_frontend_assets():
        sys.exit(1)

    Logger.success("Configuración validada correctamente")

    run_server()


if __name__ == "__main__":
    main()
