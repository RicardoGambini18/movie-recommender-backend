from config.database import db
from sqlalchemy import Column, Integer, Text


class User(db.Model):
    __tablename__ = 'User'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Text, nullable=False)
    email = Column(Text, unique=True, nullable=False)
    image = Column(Text, nullable=True)

    def __repr__(self):
        return f'<User {self.id}: {self.name} ({self.email})>'

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'image': self.image
        }
