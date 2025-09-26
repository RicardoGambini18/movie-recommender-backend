from config.database import db
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, Text


class Language(db.Model):
    __tablename__ = 'languages'

    id = Column(Integer, primary_key=True, autoincrement=True)
    iso6391 = Column(Text, unique=True, nullable=False)
    name = Column(Text, nullable=False)

    movies = relationship("Movie", back_populates="original_language")

    def __repr__(self):
        return f'<Language {self.id}: {self.name} ({self.iso6391})>'

    def to_dict(self):
        return {
            'id': self.id,
            'iso6391': self.iso6391,
            'name': self.name
        }
