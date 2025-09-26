from config.database import db
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, ForeignKey


class MovieProductionCountry(db.Model):
    __tablename__ = 'movie_production_countries'

    movie_id = Column(Integer, ForeignKey(
        'movies.id', ondelete='CASCADE'), primary_key=True)
    country_id = Column(Integer, ForeignKey(
        'countries.id', ondelete='CASCADE'), primary_key=True)

    movie = relationship("Movie", back_populates="production_countries")
    country = relationship("Country", back_populates="movies")

    def __repr__(self):
        return f'<MovieProductionCountry {self.movie_id}-{self.country_id}>'

    def to_dict(self):
        return {
            'movie_id': self.movie_id,
            'country_id': self.country_id
        }
