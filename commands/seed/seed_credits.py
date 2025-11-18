import csv
from config.logging import Logger
from models import CastMember, CrewMember, MovieCastMember, MovieCrewMember
from commands.seed.utils import is_row_valid, validate_and_convert_int, validate_and_convert_list, validate_and_convert_gender, validate_and_convert_department, process_batch


def seed_credits(movies_mapping: dict):
    cast_members_mapping = {}
    crew_members_mapping = {}
    movie_cast_members_mapping = {}
    movie_crew_members_mapping = {}

    required_fields = ['id']
    skipped_cast_members = 0
    skipped_crew_members = 0

    with open('data/credits.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for row in reader:
            if not is_row_valid(row, required_fields):
                continue

            movie_id = validate_and_convert_int(row['id'])
            cast = validate_and_convert_list(row['cast'])
            crew = validate_and_convert_list(row['crew'])

            if movie_id is None or cast is None or crew is None:
                continue

            movie = movies_mapping.get(movie_id)

            if movie is None:
                continue

            for cast_member in cast:
                if not is_row_valid(cast_member, ['id', 'name']):
                    skipped_cast_members += 1
                    continue

                cast_member_id = validate_and_convert_int(cast_member['id'])
                cast_member_order = validate_and_convert_int(
                    cast_member['order'])

                if cast_member_id is None or cast_member_order is None:
                    skipped_cast_members += 1
                    continue

                cast_member_gender = None

                if cast_member.get('gender') is not None:
                    cast_member_gender = validate_and_convert_gender(
                        cast_member['gender'])

                cast_members_mapping[cast_member_id] = {
                    'id': cast_member_id,
                    'name': cast_member['name'],
                    'gender': cast_member_gender,
                    'profile_path': cast_member.get('profile_path') if cast_member.get('profile_path') else None,
                    'character': cast_member.get('character') if cast_member.get('character') else None,
                    'character_es': None,
                    'order': cast_member_order,
                }

                movie_cast_member_id = f"{movie['id']}-{cast_member_id}"

                movie_cast_members_mapping[movie_cast_member_id] = {
                    'movie_id': movie['id'],
                    'cast_member_id': cast_member_id,
                }

            for crew_member in crew:
                if not is_row_valid(crew_member, ['id', 'name', 'department', 'job']):
                    skipped_crew_members += 1
                    continue

                crew_member_id = validate_and_convert_int(crew_member['id'])
                crew_member_department = validate_and_convert_department(
                    crew_member['department'])

                if crew_member_id is None or crew_member_department is None:
                    skipped_crew_members += 1
                    continue

                crew_member_gender = None

                if crew_member.get('gender') is not None:
                    crew_member_gender = validate_and_convert_gender(
                        crew_member['gender'])

                crew_members_mapping[crew_member_id] = {
                    'id': crew_member_id,
                    'name': crew_member['name'],
                    'gender': crew_member_gender,
                    'profile_path': crew_member.get('profile_path') if crew_member.get('profile_path') else None,
                    'department': crew_member_department,
                    'job': crew_member['job'],
                    'job_es': None,
                }

                movie_crew_member_id = f"{movie['id']}-{crew_member_id}"

                movie_crew_members_mapping[movie_crew_member_id] = {
                    'movie_id': movie['id'],
                    'crew_member_id': crew_member_id,
                }

    Logger.info(
        f"Ingresando {len(cast_members_mapping)} miembros de reparto a la base de datos")

    def insert_cast_member_batch(cast_members: list[dict], batch_number, batch_size):
        Logger.info(
            f"Ingresando lote {batch_number} ({batch_size} miembros de reparto) a la base de datos")
        CastMember.bulk_insert(cast_members)

    def insert_movie_cast_member_batch(movie_cast_members: list[dict], batch_number, batch_size):
        Logger.info(
            f"Ingresando lote {batch_number} ({batch_size} relaciones entre películas y miembros de reparto) a la base de datos")
        MovieCastMember.bulk_insert(movie_cast_members)

    process_batch(
        list(cast_members_mapping.values()), insert_cast_member_batch)
    process_batch(
        list(movie_cast_members_mapping.values()), insert_movie_cast_member_batch)

    Logger.success(
        "Miembros de reparto ingresados a la base de datos correctamente")
    if skipped_cast_members > 0:
        Logger.warning(
            f"Se han saltado {skipped_cast_members} miembros de reparto inválidos")

    Logger.info(
        f"Ingresando {len(crew_members_mapping)} miembros del equipo a la base de datos")

    def insert_crew_member_batch(crew_members: list[dict], batch_number, batch_size):
        Logger.info(
            f"Ingresando lote {batch_number} ({batch_size} miembros del equipo) a la base de datos")
        CrewMember.bulk_insert(crew_members)

    def insert_movie_crew_member_batch(movie_crew_members: list[dict], batch_number, batch_size):
        Logger.info(
            f"Ingresando lote {batch_number} ({batch_size} relaciones entre películas y miembros del equipo) a la base de datos")
        MovieCrewMember.bulk_insert(movie_crew_members)

    process_batch(
        list(crew_members_mapping.values()), insert_crew_member_batch)
    process_batch(
        list(movie_crew_members_mapping.values()), insert_movie_crew_member_batch)

    Logger.success(
        "Miembros del equipo ingresados a la base de datos correctamente")
    if skipped_crew_members > 0:
        Logger.warning(
            f"Se han saltado {skipped_crew_members} miembros del equipo inválidos")
