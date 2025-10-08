import time
import requests
from models import Movie
from enums import MovieStatus
from config.database import db
from config.logging import Logger
from config.environment import Environment

DELAY_BETWEEN_REQUESTS = 0.025


def parse_movie_status(status):
    if status == 'Released':
        return MovieStatus.RELEASED
    elif status == 'Rumored':
        return MovieStatus.RUMORED
    elif status == 'Post Production':
        return MovieStatus.POST_PRODUCTION
    elif status == 'In Production':
        return MovieStatus.IN_PRODUCTION
    elif status == 'Planned':
        return MovieStatus.PLANNED
    elif status == 'Canceled':
        return MovieStatus.CANCELED
    else:
        return None


def data_update():
    TMDB_API_KEY = Environment.TMDB_API_KEY()

    if not TMDB_API_KEY:
        Logger.error("La variable de entorno TMDB_API_KEY no está seteada")
        return

    Logger.info("Actualizando datos de las películas usando la API de TMDB")

    movies = Movie.query.all()

    for movie in movies:
        movie_data = movie.to_dict()
        movie_id = movie_data['tmdb_id']
        Logger.info(f"Actualizando película con ID {movie_id}")

        tmdb_api_url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}&language=es-ES"
        response = requests.get(tmdb_api_url)

        if response.status_code == 429:
            retry_after = response.headers.get('Retry-After', 5)
            Logger.warning(
                f"Límite de peticiones excedido (429). Esperando {retry_after} segundos.")
            time.sleep(int(retry_after))

            response = requests.get(tmdb_api_url)

            if response.status_code != 200:
                Logger.error(
                    f"Error persistente (después de reintento) actualizando película con ID {movie_id}. Status: {response.status_code}")

                time.sleep(DELAY_BETWEEN_REQUESTS * 10)
                continue

        elif response.status_code != 200:
            Logger.error(
                f"Error actualizando película con ID {movie_id}. Status: {response.status_code}")
            time.sleep(DELAY_BETWEEN_REQUESTS * 5)
            continue

        updated_movie = response.json()

        parsed_movie_status = parse_movie_status(updated_movie['status'])

        movie.status = parsed_movie_status if parsed_movie_status else movie.status
        movie.budget = updated_movie['budget'] if updated_movie['budget'] else movie.budget
        movie.title_es = updated_movie['title'] if updated_movie['title'] else movie.title_es
        movie.revenue = updated_movie['revenue'] if updated_movie['revenue'] else movie.revenue
        movie.homepage = updated_movie['homepage'] if updated_movie['homepage'] else movie.homepage
        movie.tagline_es = updated_movie['tagline'] if updated_movie['tagline'] else movie.tagline_es
        movie.overview_es = updated_movie['overview'] if updated_movie['overview'] else movie.overview_es
        movie.poster_path = updated_movie['poster_path'] if updated_movie[
            'poster_path'] else movie.poster_path

        db.session.commit()
        Logger.success(
            f"Película con ID {movie_id} actualizada correctamente")

        time.sleep(DELAY_BETWEEN_REQUESTS)

    Logger.success("Datos de las películas actualizados correctamente")
