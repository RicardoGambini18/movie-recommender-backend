from models import Movie
from flask import request
from flasgger import swag_from
from config.logging import Logger
from flask import Blueprint, jsonify
from core.data_structure_algorithm_registry import DataStructureAlgorithmRegistryManager
from core.one_dimensional_array_search_algorithm import OneDimensionalArraySearchAlgorithm

movies_bp = Blueprint('movies', __name__)

registry_manager = DataStructureAlgorithmRegistryManager(
    registries=[OneDimensionalArraySearchAlgorithm]
)


@swag_from('../docs/movies/get-movies-search-data-structures.yaml')
@movies_bp.route('/movies/search/data-structures', methods=['GET'])
def get_movies_search_data_structures():
    try:
        return jsonify(registry_manager.get_options())
    except Exception as e:
        error_message = f"Error al obtener el registro de estruturas de datos: {e}"
        Logger.error(error_message)
        return jsonify({"error": error_message}), 500


@swag_from('../docs/movies/search_movie.yaml')
@movies_bp.route('/movies/search', methods=['GET'])
def search_movie():
    try:
        movie_id = int(request.args.get('movie_id'))
        algorithm_key = request.args.get('algorithm_key')
        data_structure_key = request.args.get('data_structure_key')

        if movie_id is None or algorithm_key is None or data_structure_key is None:
            return jsonify({"error": "Parámetros inválidos"}), 400

        movies = Movie.query.all()
        movies_data = [movie.to_dict() for movie in movies]

        algorithm_method = registry_manager.get_algorithm_method(
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
