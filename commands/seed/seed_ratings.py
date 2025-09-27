import csv
from faker import Faker
from datetime import datetime
from models import User, Rating
from utils import BatchProcessor
from config.logging import Logger
from commands.seed.utils import is_row_valid, validate_and_convert_int, validate_and_convert_float, get_email, get_image_url


faker = Faker('es_ES')


def seed_ratings(movies_mapping: dict):
    users_mapping = {}
    ratings_mapping = {}
    valid_movie_ids = set()

    skipped_rows = 0
    required_fields = ['userId', 'movieId', 'rating']

    for movie in movies_mapping.values():
        valid_movie_ids.add(movie['id'])

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

            if movie_id not in valid_movie_ids:
                skipped_rows += 1
                continue

            if not users_mapping.get(user_id):
                user_name = faker.name()

                users_mapping[user_id] = {
                    'id': user_id,
                    'name': user_name,
                    'email': get_email(user_name),
                    'image': get_image_url(
                        width=400,
                        height=400,
                        blur=faker.random_int(min=0, max=2),
                        grayscale=faker.boolean(chance_of_getting_true=25),
                    ),
                }

            rating_id = f'{user_id}-{movie_id}'

            ratings_mapping[rating_id] = {
                'user_id': user_id,
                'movie_id': movie_id,
                'rating': int(rating * 2),
                'timestamp': faker.date_time_between(
                    start_date=datetime(2022, 1, 1),
                    end_date=datetime(2025, 6, 1)
                ),
            }

    Logger.success(
        f"Ingresando {len(users_mapping)} usuarios a la base de datos")

    User.bulk_insert(users_mapping.values())

    Logger.success(
        f"Usuarios ingresados a la base de datos correctamente")

    Logger.info(
        f"Ingresando {len(ratings_mapping)} ratings a la base de datos")

    def insert_rating_batch(ratings: list[dict], batch_number, batch_size):
        Logger.info(
            f"Ingresando lote {batch_number} ({batch_size} ratings) a la base de datos")
        Rating.bulk_insert(ratings)

    BatchProcessor.process(list(ratings_mapping.values()), insert_rating_batch)

    Logger.success(
        f"Ratings ingresados a la base de datos correctamente")
    if skipped_rows > 0:
        Logger.warning(
            f"Se han saltado {skipped_rows} ratings inválidos")
