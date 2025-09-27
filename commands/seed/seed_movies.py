import csv
from utils import BatchProcessor
from config.logging import Logger
from models import Language, Collection, Movie, Genre, MovieGenre, Company, MovieProductionCompany, Country, MovieProductionCountry
from commands.seed.utils import is_row_valid, validate_and_convert_int, validate_and_convert_dict, validate_and_convert_list, validate_and_convert_boolean, validate_and_convert_movie_status, validate_and_convert_date


def seed_movies(links_mapping: dict, ratings_mapping: dict):
    movies_mapping = {}
    genres_mapping = {}
    countries_mapping = {}
    companies_mapping = {}
    languages_mapping = {}
    collections_mapping = {}

    movie_genres_mapping = {}
    movie_production_companies_mapping = {}
    movie_production_countries_mapping = {}

    country_id_counter = 0
    language_id_counter = 0

    skipped_movies = 0
    skipped_genres = 0
    skipped_companies = 0
    skipped_countries = 0
    skipped_collections = 0
    required_fields = [
        'id',
        'status',
        'overview',
        'release_date',
        'original_title',
        'original_language',
    ]

    with open('data/movies_metadata.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for row in reader:
            if not is_row_valid(row, required_fields):
                skipped_movies += 1
                continue

            movie_id = validate_and_convert_int(row['id'])
            genres = validate_and_convert_list(row['genres'])
            adult = validate_and_convert_boolean(row['adult'])
            spoken_languages = validate_and_convert_list(
                row['spoken_languages'])
            companies = validate_and_convert_list(
                row['production_companies'])
            countries = validate_and_convert_list(
                row['production_countries'])
            status = validate_and_convert_movie_status(
                row['status'])
            release_date = validate_and_convert_date(row['release_date'])

            if movie_id is None or release_date is None or status is None or genres is None or adult is None or adult == True or spoken_languages is None or companies is None or countries is None:
                skipped_movies += 1
                continue

            link = links_mapping[movie_id]

            if link is None:
                skipped_movies += 1
                continue

            original_language = None

            for language in spoken_languages:
                if not is_row_valid(language, ['iso_639_1', 'name']):
                    continue

                if language['iso_639_1'] == row['original_language']:
                    original_language = language

            if original_language is None:
                skipped_movies += 1
                continue

            existing_language = languages_mapping.get(
                original_language['iso_639_1'])
            original_language_id = None

            if existing_language is None:
                language_id_counter += 1
                original_language_id = language_id_counter
            else:
                original_language_id = existing_language['id']

            languages_mapping[original_language['iso_639_1']] = {
                'id': original_language_id,
                'name': original_language['name'],
                'iso6391': original_language['iso_639_1'],
            }

            collection_id = None
            belongs_to_collection = validate_and_convert_dict(
                row['belongs_to_collection'])

            if belongs_to_collection is not None:
                if not is_row_valid(belongs_to_collection, ['id', 'name']):
                    skipped_collections += 1
                else:
                    collection_id = validate_and_convert_int(
                        belongs_to_collection['id'])

                    if collection_id is None:
                        skipped_collections += 1
                    else:
                        collections_mapping[collection_id] = {
                            'name_es': None,
                            'id': collection_id,
                            'name': belongs_to_collection['name'],
                            'poster_path': row.get('poster_path') if row.get('poster_path') else None,
                            'backdrop_path': row.get('backdrop_path') if row.get('backdrop_path') else None,
                        }

            for genre in genres:
                if not is_row_valid(genre, ['id', 'name']):
                    skipped_genres += 1
                    continue

                genre_id = validate_and_convert_int(genre['id'])

                if genre_id is None:
                    skipped_genres += 1
                    continue

                genres_mapping[genre_id] = {
                    'id': genre_id,
                    'name_es': None,
                    'name': genre['name'],
                }

                movie_genre_record_id = f'{link['movie_id']}-{genre_id}'

                movie_genres_mapping[movie_genre_record_id] = {
                    'genre_id': genre_id,
                    'movie_id': link['movie_id'],
                }

            for company in companies:
                if not is_row_valid(company, ['id', 'name']):
                    skipped_companies += 1
                    continue

                company_id = validate_and_convert_int(company['id'])

                if company_id is None:
                    skipped_companies += 1
                    continue

                existing_company = companies_mapping.get(company['name'])
                if existing_company is not None:
                    company_id = existing_company['id']

                companies_mapping[company['name']] = {
                    'id': company_id,
                    'name': company['name'],
                }

                movie_production_company_record_id = f'{link['movie_id']}-{company_id}'

                movie_production_companies_mapping[movie_production_company_record_id] = {
                    'company_id': company_id,
                    'movie_id': link['movie_id'],
                }

            for country in countries:
                if not is_row_valid(country, ['iso_3166_1', 'name']):
                    skipped_countries += 1
                    continue

                existing_country = countries_mapping.get(country['iso_3166_1'])
                country_id = None

                if existing_country is None:
                    country_id_counter += 1
                    country_id = country_id_counter
                else:
                    country_id = existing_country['id']

                countries_mapping[country['iso_3166_1']] = {
                    'name_es': None,
                    'id': country_id,
                    'name': country['name'],
                    'iso31661': country['iso_3166_1'],
                }

                movie_production_country_record_id = f'{link['movie_id']}-{country_id}'

                movie_production_countries_mapping[movie_production_country_record_id] = {
                    'country_id': country_id,
                    'movie_id': link['movie_id'],
                }

            ratings = ratings_mapping.get(link['movie_id'], [])

            vote_count = len(ratings)
            vote_sum = 0

            for rating in ratings:
                vote_sum += rating['rating'] * 2

            vote_average = vote_sum / vote_count if vote_count > 0 else 0

            budget = None if validate_and_convert_int(
                row['budget']) == 0 else validate_and_convert_int(row['budget'])
            revenue = None if validate_and_convert_int(
                row['revenue']) == 0 else validate_and_convert_int(row['revenue'])

            movies_mapping[movie_id] = {
                'id': link['movie_id'],
                'status': status,
                'budget': budget,
                'revenue': revenue,
                'homepage': row.get('homepage') if row.get('homepage') else None,
                'tmdb_id': link['tmdb_id'],
                'imdb_id': link['imdb_id'],
                'title': row['original_title'],
                'title_es': row['original_title'] if row['original_language'] == 'es' else None,
                'overview': row['overview'],
                'overview_es': None,
                'poster_path': row.get('poster_path') if row.get('poster_path') else None,
                'release_date': release_date,
                'tagline': row.get('tagline') if row.get('tagline') else None,
                'tagline_es': None,
                'vote_average': vote_average,
                'vote_count': vote_count,
                'original_language_id': original_language_id,
                'collection_id': collection_id,
            }

    Logger.info(
        f"Ingresando {len(languages_mapping)} lenguajes a la base de datos")

    Language.bulk_insert(languages_mapping.values())

    Logger.success("Lenguajes ingresados a la base de datos correctamente")

    Logger.info(
        f"Ingresando {len(collections_mapping)} colecciones a la base de datos")

    Collection.bulk_insert(collections_mapping.values())

    Logger.success(
        "Colecciones ingresadas a la base de datos correctamente")
    if skipped_collections > 0:
        Logger.warning(
            f"Se han saltado {skipped_collections} colecciones inválidas")

    Logger.info(
        f"Ingresando {len(movies_mapping)} películas por lotes a la base de datos")

    def insert_movie_batch(movies: list[dict], batch_number, batch_size):
        Logger.info(
            f"Ingresando lote {batch_number} ({batch_size} películas) a la base de datos")
        Movie.bulk_insert(movies)

    BatchProcessor.process(list(movies_mapping.values()), insert_movie_batch)

    Logger.success("Películas ingresadas a la base de datos correctamente")
    if skipped_movies > 0:
        Logger.warning(
            f"Se han saltado {skipped_movies} películas inválidas")

    Logger.info(
        f"Ingresando {len(genres_mapping)} géneros a la base de datos")

    Genre.bulk_insert(genres_mapping.values())
    MovieGenre.bulk_insert(movie_genres_mapping.values())

    Logger.success("Géneros ingresados a la base de datos correctamente")
    if skipped_genres > 0:
        Logger.warning(
            f"Se han saltado {skipped_genres} géneros inválidos")

    Logger.info(
        f"Ingresando {len(companies_mapping)} compañías a la base de datos")

    Company.bulk_insert(companies_mapping.values())
    MovieProductionCompany.bulk_insert(
        movie_production_companies_mapping.values())

    Logger.success(
        "Compañías ingresadas a la base de datos correctamente")
    if skipped_companies > 0:
        Logger.warning(
            f"Se han saltado {skipped_companies} compañías inválidas")

    Logger.info(
        f"Ingresando {len(countries_mapping)} países a la base de datos")

    Country.bulk_insert(countries_mapping.values())
    MovieProductionCountry.bulk_insert(
        movie_production_countries_mapping.values())

    Logger.success("Países ingresados a la base de datos correctamente")
    if skipped_countries > 0:
        Logger.warning(
            f"Se han saltado {skipped_countries} países inválidos")

    return movies_mapping
