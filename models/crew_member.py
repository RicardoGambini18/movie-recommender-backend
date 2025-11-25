from config.database import db
from enums import Gender, Department
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, Text, Enum


class CrewMember(db.Model):
    __tablename__ = 'crew_members'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Text, nullable=False)
    gender = Column(Enum(Gender), nullable=True)
    profile_path = Column(Text, nullable=True)
    department = Column(Enum(Department), nullable=False)
    job = Column(Text, nullable=False)
    job_es = Column(Text, nullable=True)

    movies = relationship("MovieCrewMember", back_populates="crew_member")

    def __repr__(self):
        return f'<CrewMember {self.id}: {self.name} - {self.job}>'

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'gender': self.gender.value if self.gender else None,
            'profile_path': self.profile_path,
            'department': self.department.value,
            'job': self.job,
            'job_es': self.job_es
        }
