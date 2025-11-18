import csv
from config.logging import Logger
from models import Keyword, MovieKeyword
from commands.seed.utils import is_row_valid, validate_and_convert_int, validate_and_convert_list, process_batch


def seed_keywords(movies_mapping: dict):
    keywords_mapping = {}
    movie_keywords_mapping = {}

    skipped_rows = 0
    required_fields = ['id']

    with open('data/keywords.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for row in reader:
            if not is_row_valid(row, required_fields):
                skipped_rows += 1
                continue

            movie_id = validate_and_convert_int(row['id'])
            keywords = validate_and_convert_list(row['keywords'])

            if movie_id is None or keywords is None:
                skipped_rows += 1
                continue

            movie = movies_mapping.get(movie_id)

            if movie is None:
                skipped_rows += 1
                continue

            for keyword in keywords:
                if not is_row_valid(keyword, ['id', 'name']):
                    skipped_rows += 1
                    continue

                keyword_id = validate_and_convert_int(keyword['id'])

                if keyword_id is None:
                    skipped_rows += 1
                    continue

                keywords_mapping[keyword_id] = {
                    'id': keyword_id,
                    'name': keyword['name'],
                    'name_es': None,
                }

                movie_keyword_id = f"{movie['id']}-{keyword_id}"

                movie_keywords_mapping[movie_keyword_id] = {
                    'movie_id': movie['id'],
                    'keyword_id': keyword_id,
                }

    Logger.info(
        f"Ingresando {len(keywords_mapping)} palabras clave por lotes a la base de datos")

    def insert_keyword_batch(keywords: list[dict], batch_number, batch_size):
        Logger.info(
            f"Ingresando lote {batch_number} ({batch_size} palabras clave) a la base de datos")
        Keyword.bulk_insert(keywords)

    def insert_movie_keyword_batch(movie_keywords: list[dict], batch_number, batch_size):
        Logger.info(
            f"Ingresando lote {batch_number} ({batch_size} relaciones entre películas y palabras clave) a la base de datos")
        MovieKeyword.bulk_insert(movie_keywords)

    process_batch(
        list(keywords_mapping.values()), insert_keyword_batch)
    process_batch(
        list(movie_keywords_mapping.values()), insert_movie_keyword_batch)

    Logger.success(
        "Palabras clave ingresadas a la base de datos correctamente")
    if skipped_rows > 0:
        Logger.warning(
            f"Se han saltado {skipped_rows} palabras clave inválidas")
