from enums import MovieStatus
from config.database import db
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, Text, Float, Date, BigInteger, ForeignKey, Enum


class Movie(db.Model):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True, autoincrement=True)
    status = Column(Enum(MovieStatus), nullable=False)
    budget = Column(BigInteger, nullable=True)
    revenue = Column(BigInteger, nullable=True)
    homepage = Column(Text, nullable=True)
    tmdb_id = Column(Integer, unique=True, nullable=False)
    imdb_id = Column(Integer, unique=True, nullable=False)
    title = Column(Text, nullable=False)
    title_es = Column(Text, nullable=True)
    overview = Column(Text, nullable=False)
    overview_es = Column(Text, nullable=True)
    poster_path = Column(Text, nullable=True)
    release_date = Column(Date, nullable=False)
    tagline = Column(Text, nullable=True)
    tagline_es = Column(Text, nullable=True)
    vote_average = Column(Float, nullable=False)
    vote_count = Column(Integer, nullable=False)

    original_language_id = Column(
        Integer, ForeignKey('languages.id'), nullable=False)
    collection_id = Column(Integer, ForeignKey(
        'collections.id'), nullable=True)

    original_language = relationship("Language", back_populates="movies")
    collection = relationship("Collection", back_populates="movies")
    genres = relationship("MovieGenre", back_populates="movie")
    production_companies = relationship(
        "MovieProductionCompany", back_populates="movie")
    production_countries = relationship(
        "MovieProductionCountry", back_populates="movie")
    keywords = relationship("MovieKeyword", back_populates="movie")
    cast = relationship("MovieCastMember", back_populates="movie")
    crew = relationship("MovieCrewMember", back_populates="movie")
    ratings = relationship("Rating", back_populates="movie")

    def __repr__(self):
        return f'<Movie {self.id}: {self.title}>'

    def to_dict(self):
        return {
            'id': self.id,
            'status': self.status.value,
            'budget': self.budget,
            'revenue': self.revenue,
            'homepage': self.homepage,
            'tmdb_id': self.tmdb_id,
            'imdb_id': self.imdb_id,
            'title': self.title,
            'title_es': self.title_es,
            'overview': self.overview,
            'overview_es': self.overview_es,
            'poster_path': self.poster_path,
            'release_date': self.release_date.strftime('%Y-%m-%d'),
            'tagline': self.tagline,
            'tagline_es': self.tagline_es,
            'vote_average': self.vote_average,
            'vote_count': self.vote_count,
            'original_language_id': self.original_language_id,
            'collection_id': self.collection_id
        }
