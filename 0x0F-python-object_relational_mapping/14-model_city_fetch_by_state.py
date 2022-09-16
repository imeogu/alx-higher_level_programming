#!/usr/bin/python3
''' Prints all City objects from the database hbtn_0e_14_usa
    It takes 3 arguments - 1st arg = user
                         - 2nd arg = passwd
                         - 3rd arg = database_name
'''
import sys

from sqlalchemy.sql.elements import Null
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


#engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]));
engine = create_engine('mysql+mysqldb://root:Lilstex4good95@localhost:3306/hbtn_0e_14_usa', pool_pre_ping=True);

Session = sessionmaker(bind=engine);
session = Session();

for city, state in session.query(City, State).filter(City.state_id == State.id).order_by(City.id):
    print('{}: ({}) {}'.format(state.name, city.id, city.name));