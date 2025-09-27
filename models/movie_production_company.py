from config.database import db
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, ForeignKey


class MovieProductionCompany(db.Model):
    __tablename__ = 'movie_production_companies'

    movie_id = Column(Integer, ForeignKey(
        'movies.id', ondelete='CASCADE'), primary_key=True)
    company_id = Column(Integer, ForeignKey(
        'companies.id', ondelete='CASCADE'), primary_key=True)

    movie = relationship("Movie", back_populates="production_companies")
    company = relationship("Company", back_populates="movies")

    def __repr__(self):
        return f'<MovieProductionCompany {self.movie_id}-{self.company_id}>'

    def to_dict(self):
        return {
            'movie_id': self.movie_id,
            'company_id': self.company_id
        }

    @staticmethod
    def bulk_insert(movie_production_companies: list[dict]):
        db.session.bulk_insert_mappings(
            MovieProductionCompany, movie_production_companies)
        db.session.commit()
