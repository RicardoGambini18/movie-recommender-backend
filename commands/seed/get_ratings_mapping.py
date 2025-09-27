import csv
from config.logging import Logger
from commands.seed.utils import is_row_valid, validate_and_convert_int, validate_and_convert_float


def get_ratings_mapping():
    Logger.info("Creando mapa de ratings")

    skipped_rows = 0
    ratings_mapping = {}
    required_fields = ['userId', 'movieId', 'rating']

    with open('data/ratings.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for row in reader:
            if not is_row_valid(row, required_fields):
                skipped_rows += 1
                continue

            user_id = validate_and_convert_int(row['userId'])
            rating = validate_and_convert_float(row['rating'])
            movie_id = validate_and_convert_int(row['movieId'])

            if user_id is None or movie_id is None or rating is None:
                skipped_rows += 1
                continue

            rating_list = ratings_mapping.get(movie_id, [])

            rating_list.append({
                'rating': rating,
                'user_id': user_id,
                'movie_id': movie_id,
            })

            ratings_mapping[movie_id] = rating_list

    Logger.success(
        f"Mapa de ratings creado correctamente")

    if skipped_rows > 0:
        Logger.warning(
            f"Se han saltado {skipped_rows} ratings inválidos")

    return ratings_mapping
