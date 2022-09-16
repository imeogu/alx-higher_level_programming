#!/usr/bin/python3
# Defines a State model and inherits from SQLAlchemy Base and links to the MySQL table states.

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base();

class State(Base):
    '''
    Represents a state for a MySQL database.
    __tablename__ : The name of the MySQL table to store States.
    id: The state's id.
    name: The state's name.
    '''

    __tablename__ = 'states';
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True, nullable=False);
    name = Column(String(128), nullable=False);

    def __init__(self, name):
        self.name = name
