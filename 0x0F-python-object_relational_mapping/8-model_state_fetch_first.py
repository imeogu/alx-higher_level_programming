#!/usr/bin/python3
''' Prints the first State object from the database hbtn_0e_6_usa
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

state = session.query(State).order_by(State.id).first();
if (state is None):
    print('Nothing')
print('{}: {}'.format(state.id, state.name));