#!/usr/bin/python3
''' Lists all State objects from the database hbtn_0e_6_usa
    It takes 3 arguments - 1st arg = user
                         - 2nd arg = passwd
                         - 3rd arg = database_name
'''
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]));

Session = sessionmaker(bind=engine);
session = Session();

states = session.query(State).order_by(State.id)
for state in states:
    print('{}: {}'.format(state.id, state.name));