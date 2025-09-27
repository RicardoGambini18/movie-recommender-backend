from config.database import db
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, ForeignKey


class MovieKeyword(db.Model):
    __tablename__ = 'movie_keywords'

    movie_id = Column(Integer, ForeignKey(
        'movies.id', ondelete='CASCADE'), primary_key=True)
    keyword_id = Column(Integer, ForeignKey(
        'keywords.id', ondelete='CASCADE'), primary_key=True)

    movie = relationship("Movie", back_populates="keywords")
    keyword = relationship("Keyword", back_populates="movies")

    def __repr__(self):
        return f'<MovieKeyword {self.movie_id}-{self.keyword_id}>'

    def to_dict(self):
        return {
            'movie_id': self.movie_id,
            'keyword_id': self.keyword_id
        }

    @staticmethod
    def bulk_insert(movie_keywords: list[dict]):
        db.session.bulk_insert_mappings(MovieKeyword, movie_keywords)
        db.session.commit()
