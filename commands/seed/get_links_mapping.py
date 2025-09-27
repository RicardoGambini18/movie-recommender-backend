import csv
from config.logging import Logger
from commands.seed.utils import is_row_valid, validate_and_convert_int


def get_links_mapping():
    Logger.info("Creando mapa de links")

    skipped_rows = 0
    links_mapping = {}
    required_fields = ['movieId', 'tmdbId', 'imdbId']

    with open('data/links.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for row in reader:
            if not is_row_valid(row, required_fields):
                skipped_rows += 1
                continue

            tmdb_id = validate_and_convert_int(row['tmdbId'])
            imdb_id = validate_and_convert_int(row['imdbId'])
            movie_id = validate_and_convert_int(row['movieId'])

            if movie_id is None or tmdb_id is None or imdb_id is None:
                skipped_rows += 1
                continue

            links_mapping[tmdb_id] = {
                'tmdb_id': tmdb_id,
                'imdb_id': imdb_id,
                'movie_id': movie_id,
            }

    Logger.success("Mapa de links creado correctamente")

    if skipped_rows > 0:
        Logger.warning(
            f"Se han saltado {skipped_rows} links inválidos")

    return links_mapping
