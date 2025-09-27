from config.database import db
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, ForeignKey


class MovieGenre(db.Model):
    __tablename__ = 'movie_genres'

    movie_id = Column(Integer, ForeignKey(
        'movies.id', ondelete='CASCADE'), primary_key=True)
    genre_id = Column(Integer, ForeignKey(
        'genres.id', ondelete='CASCADE'), primary_key=True)

    movie = relationship("Movie", back_populates="genres")
    genre = relationship("Genre", back_populates="movies")

    def __repr__(self):
        return f'<MovieGenre {self.movie_id}-{self.genre_id}>'

    def to_dict(self):
        return {
            'movie_id': self.movie_id,
            'genre_id': self.genre_id
        }

    @staticmethod
    def bulk_insert(movie_genres: list[dict]):
        db.session.bulk_insert_mappings(MovieGenre, movie_genres)
        db.session.commit()
