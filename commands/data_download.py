import gdown
from pathlib import Path
from config.logging import Logger

DATA_DIR_PATH = "data"
GOOGLE_DRIVE_URL = "https://drive.google.com/uc?export=download&id="

DATASET_FILES = [
    {
        "name": "credits.csv",
        "file_id": "1SkxP7MigmgG6dLyIuERS-Q6xEnlxaZgk",
    },
    {
        "name": "keywords.csv",
        "file_id": "1uf_Gb12eVoml8ZiSDRUG_GGbTfLzKT00",
    },
    {
        "name": "links.csv",
        "file_id": "107i0PtnViGPj_wj_MxVNX7ghLduKhURK",
    },
    {
        "name": "movies_metadata.csv",
        "file_id": "139L2JL55kW1Zic6Mj5yu2Fg8nZ9LQXs8",
    },
    {
        "name": "ratings.csv",
        "file_id": "1VA8WKA4d2TemJhMi910idMxx7a-i-3A5",
    }
]


def clean_data_dir():
    data_dir = Path(DATA_DIR_PATH)

    if data_dir.exists():
        for file in data_dir.iterdir():
            file.unlink()
        data_dir.rmdir()

    data_dir.mkdir(exist_ok=True)


def get_download_url(file_id: str):
    return f"{GOOGLE_DRIVE_URL}{file_id}"


def data_download():
    try:
        Logger.info("Descargando The Movies Dataset")

        clean_data_dir()

        for dataset_file in DATASET_FILES:
            name = dataset_file['name']
            file_id = dataset_file['file_id']
            output_path = f"{DATA_DIR_PATH}/{name}"
            download_url = get_download_url(file_id)

            Logger.info(f"Descargando {name}")
            gdown.download(url=download_url, output=output_path)
            Logger.success(f"{name} descargado correctamente")

        Logger.success("The Movies Dataset descargado correctamente")
    except Exception as e:
        Logger.error(f"Error al descargar The Movies Dataset: {e}")
