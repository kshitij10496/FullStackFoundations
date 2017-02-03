######## Database Design #######
'''
     ____________                _______________
    |   Shelter  |              |   Menu_Item   |
    |------------|              |---------------|
    |    name    |              |     name      |
    |   address  |              | date_of_birth |
    |    city    |              |    gender     |
    |    state   |              |    weight     |
    |   zipCode  |       ------>|   shelter_id  |
    |   website  |      |        ---------------
    |     id     |------
     ------------       
'''
################################
import sys

from sqlalchemy import Column, ForeignKey, Integer, String, BigInteger, Float, Text, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Shelter(Base):
    __tablename__ = 'shelter'

    name = Column(String(80), nullable=False)
    address = Column(Text)
    city = Column(String(80))
    state = Column(String(80))
    zipCode = Column(BigInteger)
    website = Column(String(80))
    id = Column(Integer, primary_key=True)


class Puppy(Base):
    __tablename__ = 'puppy'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    date_of_birth = Column(Date)
    gender = Column(String(10))
    weight = Column(Float)
    shelter_id = Column(Integer, ForeignKey('shelter.id'))
    shelter = relationship(Shelter)

engine = create_engine('sqlite:///puppies.db')
Base.metadata.create_all(engine)
