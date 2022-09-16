#!/usr/bin/python3
'''Defines a City model and inherits from SQLAlchemy Base and links to the MySQL table city.'''

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class City(Base):
    '''
    Represents a city for a MySQL database.
    __tablename__ : The name of the MySQL table to store cities.
    id: The city id.
    name: The city name.
    state_id: The city's state id.
    '''

    __tablename__ = 'cities';
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True, nullable=False);
    name = Column(String(128), nullable=False);
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

