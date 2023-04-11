from flask import Blueprint, jsonify, request
# Blueprint: permite manjear las rutas y asociarlas para que trabaje con una colleccion de rutas
# Key
import uuid
# Entities
from models.entities.movie import Movie
# Models
from models.movie_model import MovieModel

main=Blueprint('movie_blueprint', __name__)

@main.route('/')
def get_movies():
    try:
        movies = MovieModel.get_movies()
        return jsonify(movies)
    except Exception as ex:
        return jsonify({'mensaje':str(ex)}),500
    
@main.route('/add', methods=['POST'])
def add_movie():
    try:
        title = request.json['title']
        duration = int(request.json['duration'])
        released = request.json['released']
        id = uuid.uuid4()
        movie = Movie(str(id), title, duration, released)

        affected_rows = MovieModel.add_movie(movie)
        if affected_rows == 1:
            return jsonify(movie.id)
        else:
            return jsonify({'mensaje':"Error on insert"}),500
    except Exception as ex:
        return jsonify({'mensaje':str(ex)}),500

@main.route('/update/<id>', methods=['PUT'])
def update_movie(id):
    try:
        title = request.json['title']
        duration = int(request.json['duration'])
        released = request.json['released']
        movie = Movie(id, title, duration, released)

        affected_rows = MovieModel.update_movie(movie)
        if affected_rows == 1:
            return jsonify(movie.id)
        else:
            return jsonify({'mensaje':"No movie updated"}),404
    except Exception as ex:
        return jsonify({'mensaje':str(ex)}),500

@main.route('/delete/<id>', methods=['DELETE'])
def delete_movie(id):
    try:
        movie = Movie(id)
        affected_rows = MovieModel.delete_movie(movie)
        if affected_rows == 1:
            return jsonify(movie.id)
        else:
            return jsonify({'mensaje':"No movie deleted"}),404
    except Exception as ex:
        return jsonify({'mensaje':str(ex)}),500
    