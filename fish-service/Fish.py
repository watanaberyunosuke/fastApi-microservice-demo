from sqlalchemy import Column, Integer, String

from database import Base

"""
    Model Class
"""


class Fish(Base):
    __tablename__ = 'fish'
    __table_args__ = {'schema': 'fnd_animal_crossing'}
    fish_id = Column(Integer, primary_key=True)
    name = Column(String(256))
    sell = Column(Integer)
    location = Column(String(256))
    difficulty = Column(String(256))
    size = Column(String(256))
    vision = Column(String(256))
    description = Column(String(256))
