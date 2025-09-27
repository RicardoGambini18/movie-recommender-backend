from config.database import db
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, ForeignKey


class MovieCrewMember(db.Model):
    __tablename__ = 'movie_crew_members'

    movie_id = Column(Integer, ForeignKey(
        'movies.id', ondelete='CASCADE'), primary_key=True)
    crew_member_id = Column(Integer, ForeignKey(
        'crew_members.id', ondelete='CASCADE'), primary_key=True)

    movie = relationship("Movie", back_populates="crew")
    crew_member = relationship("CrewMember", back_populates="movies")

    def __repr__(self):
        return f'<MovieCrewMember {self.movie_id}-{self.crew_member_id}>'

    def to_dict(self):
        return {
            'movie_id': self.movie_id,
            'crew_member_id': self.crew_member_id
        }

    @staticmethod
    def bulk_insert(movie_crew_members: list[dict]):
        db.session.bulk_insert_mappings(MovieCrewMember, movie_crew_members)
        db.session.commit()
