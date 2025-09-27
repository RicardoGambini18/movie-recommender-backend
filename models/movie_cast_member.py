from config.database import db
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, ForeignKey


class MovieCastMember(db.Model):
    __tablename__ = 'movie_cast_members'

    movie_id = Column(Integer, ForeignKey(
        'movies.id', ondelete='CASCADE'), primary_key=True)
    cast_member_id = Column(Integer, ForeignKey(
        'cast_members.id', ondelete='CASCADE'), primary_key=True)

    movie = relationship("Movie", back_populates="cast")
    cast_member = relationship("CastMember", back_populates="movies")

    def __repr__(self):
        return f'<MovieCastMember {self.movie_id}-{self.cast_member_id}>'

    def to_dict(self):
        return {
            'movie_id': self.movie_id,
            'cast_member_id': self.cast_member_id
        }

    @staticmethod
    def bulk_insert(movie_cast_members: list[dict]):
        db.session.bulk_insert_mappings(MovieCastMember, movie_cast_members)
        db.session.commit()
