from config.database import db
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, Text


class Collection(db.Model):
    __tablename__ = 'collections'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Text, nullable=False)
    name_es = Column(Text, nullable=True)
    poster_path = Column(Text, nullable=True)
    backdrop_path = Column(Text, nullable=True)

    movies = relationship("Movie", back_populates="collection")

    def __repr__(self):
        return f'<Collection {self.id}: {self.name}>'

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'name_es': self.name_es,
            'poster_path': self.poster_path,
            'backdrop_path': self.backdrop_path
        }
