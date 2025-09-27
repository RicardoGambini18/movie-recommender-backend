from config.database import db
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, DateTime, ForeignKey


class Rating(db.Model):
    __tablename__ = 'ratings'

    user_id = Column(Integer, ForeignKey(
        'users.id', ondelete='CASCADE'), primary_key=True)
    movie_id = Column(Integer, ForeignKey(
        'movies.id', ondelete='CASCADE'), primary_key=True)
    rating = Column(Integer, nullable=False)
    timestamp = Column(DateTime, nullable=False)

    movie = relationship("Movie", back_populates="ratings")
    user = relationship("User", back_populates="ratings")

    def __repr__(self):
        return f'<Rating User {self.user_id} -> Movie {self.movie_id}: {self.rating}>'

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'movie_id': self.movie_id,
            'rating': self.rating,
            'timestamp': self.timestamp.isoformat()
        }

    @staticmethod
    def bulk_insert(ratings: list[dict]):
        db.session.bulk_insert_mappings(Rating, ratings)
        db.session.commit()
