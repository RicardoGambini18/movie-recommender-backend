import os
import sys
import time
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
    in_venv = hasattr(sys, 'real_prefix') or (
        hasattr(sys, 'base_prefix') and sys.prefix != sys.base_prefix
    )

    if in_venv:
        Logger.success("Ejecutando dentro del entorno virtual")
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


def open_browser(port):
    time.sleep(1.5)
    url = f"http://localhost:{port}"
    Logger.info(f"Abriendo aplicación en el navegador")
    webbrowser.open(url)


def run_server():
    from server import app, port, mode

    browser_thread = threading.Thread(
        target=open_browser, args=(port,), daemon=True)
    browser_thread.start()

    Logger.info(
        f"Iniciando servidor en modo {mode} (Debug: Desactivado) en el puerto {port}")
    Logger.info(f"Aplicación disponible en http://localhost:{port}")

    app.run(debug=False, port=port)


def main():
    Logger.info("Iniciando Algolab")
    Logger.info("Validando configuración")

    if not ensure_venv():
        sys.exit(1)

    if not install_dependencies():
        sys.exit(1)

    Logger.success("Configuración validada correctamente")

    run_server()


if __name__ == "__main__":
    main()
