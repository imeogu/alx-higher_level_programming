#!/usr/bin/python3
''' Prints the State object with the name passed as argument from the database hbtn_0e_6_usa
    It takes 3 arguments - 1st arg = user
                         - 2nd arg = passwd
                         - 3rd arg = database_name
'''
import sys

from sqlalchemy.sql.elements import Null
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]));

Session = sessionmaker(bind=engine);
session = Session();

louisiana = State(name = 'Louisiana');
session.add(louisiana);

session.commit();
states = session.query(State).filter(State.name == 'Louisiana');
for state in states:
    print('{}'.format(state.id));
