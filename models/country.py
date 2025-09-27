from config.database import db
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, Text


class Country(db.Model):
    __tablename__ = 'countries'

    id = Column(Integer, primary_key=True, autoincrement=True)
    iso31661 = Column(Text, unique=True, nullable=False)
    name = Column(Text, nullable=False)
    name_es = Column(Text, nullable=True)

    movies = relationship("MovieProductionCountry", back_populates="country")

    def __repr__(self):
        return f'<Country {self.id}: {self.name} ({self.iso31661})>'

    def to_dict(self):
        return {
            'id': self.id,
            'iso31661': self.iso31661,
            'name': self.name,
            'name_es': self.name_es
        }

    @staticmethod
    def bulk_insert(countries: list[dict]):
        db.session.bulk_insert_mappings(Country, countries)
        db.session.commit()
