from config.database import db
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, Text


class Keyword(db.Model):
    __tablename__ = 'keywords'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Text, unique=True, nullable=False)
    name_es = Column(Text, nullable=True)

    movies = relationship("MovieKeyword", back_populates="keyword")

    def __repr__(self):
        return f'<Keyword {self.id}: {self.name}>'

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'name_es': self.name_es
        }

    @staticmethod
    def bulk_insert(keywords: list[dict]):
        db.session.bulk_insert_mappings(Keyword, keywords)
        db.session.commit()
