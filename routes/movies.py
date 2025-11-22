from models import Movie
from flask import request
from flasgger import swag_from
from dataclasses import asdict
from config.logger import Logger
from flask import Blueprint, jsonify
from middlewares import auth_middleware
from core.constants import MOVIES_SORT_LIMIT
from core.vector_sort_algorithm_registry import VectorSortAlgorithmRegistry
from core.vector_search_algorithm_registry import VectorSearchAlgorithmRegistry
from core.data_structure_algorithm_registry import DataStructureAlgorithmRegistryManager

movies_bp = Blueprint('movies', __name__)


sort_registry_manager = DataStructureAlgorithmRegistryManager(
    registries=[VectorSortAlgorithmRegistry]
)

search_registry_manager = DataStructureAlgorithmRegistryManager(
    registries=[VectorSearchAlgorithmRegistry]
)


@swag_from('../docs/movies/get-movies-sort-data-structures.yaml')
@movies_bp.route('/movies/sort/data-structures', methods=['GET'])
@auth_middleware
def get_movies_sort_data_structures():
    try:
        return jsonify(sort_registry_manager.get_options())
    except Exception as e:
        error_message = f"Error al obtener el registro de estruturas de datos: {e}"
        Logger.error(error_message)
        return jsonify({"error": error_message}), 500


@swag_from('../docs/movies/sort-movies.yaml')
@movies_bp.route('/movies/sort', methods=['GET'])
@auth_middleware
def sort_movies():
    try:
        algorithm_key = request.args.get('algorithm_key')
        data_structure_key = request.args.get('data_structure_key')
        include_result = request.args.get(
            'include_result', 'false').lower() == 'true'

        if algorithm_key is None or data_structure_key is None:
            return jsonify({"error": "Parámetros inválidos"}), 400

        movies = Movie.query.order_by(
            Movie.title).limit(MOVIES_SORT_LIMIT).all()
        movies_data = [movie.to_dict() for movie in movies]

        algorithm_method = sort_registry_manager.get_algorithm_method(
            data=movies_data,
            algorithm_key=algorithm_key,
            data_structure_key=data_structure_key,
            value_getter=lambda movie: movie['id'],
        )

        if algorithm_method is None:
            return jsonify({"error": "Algoritmo no encontrado"}), 404

        result = algorithm_method()
        result_dict = asdict(result)

        if not include_result:
            result_dict.pop('sorted_data', None)

        return jsonify(result_dict)
    except Exception as e:
        error_message = f"Error al ordenar las películas: {e}"
        Logger.error(error_message)
        return jsonify({"error": error_message}), 500


@swag_from('../docs/movies/get-movies-search-data-structures.yaml')
@movies_bp.route('/movies/search/data-structures', methods=['GET'])
@auth_middleware
def get_movies_search_data_structures():
    try:
        return jsonify(search_registry_manager.get_options())
    except Exception as e:
        error_message = f"Error al obtener el registro de estruturas de datos: {e}"
        Logger.error(error_message)
        return jsonify({"error": error_message}), 500


@swag_from('../docs/movies/search-movie.yaml')
@movies_bp.route('/movies/search', methods=['GET'])
@auth_middleware
def search_movie():
    try:
        movie_id_str = request.args.get('movie_id')
        algorithm_key = request.args.get('algorithm_key')
        data_structure_key = request.args.get('data_structure_key')
        include_result = request.args.get(
            'include_result', 'false').lower() == 'true'

        if movie_id_str is None or algorithm_key is None or data_structure_key is None:
            return jsonify({"error": "Parámetros inválidos"}), 400

        try:
            movie_id = int(movie_id_str)
        except (ValueError, TypeError):
            return jsonify({"error": "Parámetros inválidos"}), 400

        movies = Movie.query.order_by(Movie.id).all()
        movies_data = [movie.to_dict() for movie in movies]

        algorithm_method = search_registry_manager.get_algorithm_method(
            data=movies_data,
            algorithm_key=algorithm_key,
            data_structure_key=data_structure_key,
            value_getter=lambda movie: movie['id'],
        )

        if algorithm_method is None:
            return jsonify({"error": "Algoritmo no encontrado"}), 404

        result = algorithm_method(movie_id)
        result_dict = asdict(result)

        if not include_result:
            result_dict.pop('item_found', None)
            result_dict.pop('item_found_index', None)

        return jsonify(result_dict)
    except Exception as e:
        error_message = f"Error al buscar la película: {e}"
        Logger.error(error_message)
        return jsonify({"error": error_message}), 500


@swag_from('../docs/movies/get-movies.yaml')
@movies_bp.route('/movies', methods=['GET'])
@auth_middleware
def get_movies():
    try:
        movies = Movie.query.order_by(Movie.id).all()
        movies_data = [movie.to_dict() for movie in movies]
        return jsonify(movies_data)
    except Exception as e:
        error_message = f"Error al obtener películas: {e}"
        Logger.error(error_message)
        return jsonify({"error": error_message}), 500
