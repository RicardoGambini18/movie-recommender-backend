from models import Movie
from flask import request
from flasgger import swag_from
from config.logging import Logger
from flask import Blueprint, jsonify
from core.constants import MOVIES_SORT_LIMIT
from core.data_structure_algorithm_registry import DataStructureAlgorithmRegistryManager
from core.one_dimensional_array_sort_algorithm_registry import OneDimensionalArraySortAlgorithmRegistry
from core.one_dimensional_array_search_algorithm_registry import OneDimensionalArraySearchAlgorithmRegistry

movies_bp = Blueprint('movies', __name__)


sort_registry_manager = DataStructureAlgorithmRegistryManager(
    registries=[OneDimensionalArraySortAlgorithmRegistry]
)

search_registry_manager = DataStructureAlgorithmRegistryManager(
    registries=[OneDimensionalArraySearchAlgorithmRegistry]
)


@swag_from('../docs/movies/get-movies-sort-data-structures.yaml')
@movies_bp.route('/movies/sort/data-structures', methods=['GET'])
def get_movies_sort_data_structures():
    try:
        return jsonify(sort_registry_manager.get_options())
    except Exception as e:
        error_message = f"Error al obtener el registro de estruturas de datos: {e}"
        Logger.error(error_message)
        return jsonify({"error": error_message}), 500


@swag_from('../docs/movies/sort-movies.yaml')
@movies_bp.route('/movies/sort', methods=['GET'])
def sort_movies():
    try:
        algorithm_key = request.args.get('algorithm_key')
        data_structure_key = request.args.get('data_structure_key')

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

        return jsonify(algorithm_method())
    except Exception as e:
        error_message = f"Error al ordenar las películas: {e}"
        Logger.error(error_message)
        return jsonify({"error": error_message}), 500


@swag_from('../docs/movies/get-movies-search-data-structures.yaml')
@movies_bp.route('/movies/search/data-structures', methods=['GET'])
def get_movies_search_data_structures():
    try:
        return jsonify(search_registry_manager.get_options())
    except Exception as e:
        error_message = f"Error al obtener el registro de estruturas de datos: {e}"
        Logger.error(error_message)
        return jsonify({"error": error_message}), 500


@swag_from('../docs/movies/search-movie.yaml')
@movies_bp.route('/movies/search', methods=['GET'])
def search_movie():
    try:
        movie_id = int(request.args.get('movie_id'))
        algorithm_key = request.args.get('algorithm_key')
        data_structure_key = request.args.get('data_structure_key')

        if movie_id is None or algorithm_key is None or data_structure_key is None:
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

        return jsonify(algorithm_method(movie_id))
    except Exception as e:
        error_message = f"Error al buscar la película: {e}"
        Logger.error(error_message)
        return jsonify({"error": error_message}), 500


@swag_from('../docs/movies/get-movies.yaml')
@movies_bp.route('/movies', methods=['GET'])
def get_movies():
    try:
        movies = Movie.query.order_by(Movie.id).all()
        movies_data = [movie.to_dict() for movie in movies]
        return jsonify(movies_data)
    except Exception as e:
        error_message = f"Error al obtener películas: {e}"
        Logger.error(error_message)
        return jsonify({"error": error_message}), 500
