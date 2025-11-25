from enums import Gender
from config.database import db
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, Text, Enum


class CastMember(db.Model):
    __tablename__ = 'cast_members'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Text, nullable=False)
    gender = Column(Enum(Gender), nullable=True)
    profile_path = Column(Text, nullable=True)
    character = Column(Text, nullable=True)
    character_es = Column(Text, nullable=True)
    order = Column(Integer, nullable=False)

    movies = relationship("MovieCastMember", back_populates="cast_member")

    def __repr__(self):
        return f'<CastMember {self.id}: {self.name} as {self.character}>'

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'gender': self.gender.value if self.gender else None,
            'profile_path': self.profile_path,
            'character': self.character,
            'character_es': self.character_es,
            'order': self.order
        }
