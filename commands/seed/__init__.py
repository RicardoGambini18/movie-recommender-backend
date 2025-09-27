from config.logging import Logger
from commands.seed.seed_movies import seed_movies
from commands.seed.seed_credits import seed_credits
from commands.seed.seed_ratings import seed_ratings
from commands.seed.seed_keywords import seed_keywords
from commands.seed.clean_database import clean_database
from commands.seed.get_links_mapping import get_links_mapping
from commands.seed.get_ratings_mapping import get_ratings_mapping


def seed():
    try:
        Logger.info("Ingreso de The Movies Dataset a la base de datos")

        clean_database()
        links_mapping = get_links_mapping()
        ratings_mapping = get_ratings_mapping()
        movies_mapping = seed_movies(links_mapping, ratings_mapping)
        seed_keywords(movies_mapping)
        seed_credits(movies_mapping)
        seed_ratings(movies_mapping)

        Logger.success(
            "Ingreso de The Movies Dataset a la base de datos completado correctamente")
    except Exception as e:
        Logger.error(
            f"Error al ingresar The Movies Dataset a la base de datos: {e}")
