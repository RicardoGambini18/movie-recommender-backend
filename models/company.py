from config.database import db
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, Text


class Company(db.Model):
    __tablename__ = 'companies'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Text, unique=True, nullable=False)

    movies = relationship("MovieProductionCompany", back_populates="company")

    def __repr__(self):
        return f'<Company {self.id}: {self.name}>'

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }

    @staticmethod
    def bulk_insert(companies: list[dict]):
        db.session.bulk_insert_mappings(Company, companies)
        db.session.commit()
