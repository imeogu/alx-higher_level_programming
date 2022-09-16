#!/usr/bin/python3
''' Creates the State “California” with the City “San Francisco” from the database hbtn_0e_100_usa
    It takes 3 arguments - 1st arg = user
                         - 2nd arg = passwd
                         - 3rd arg = database_name
'''
import sys
from relationship_state import State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]));
    
    Session = sessionmaker(bind=engine);
    session = Session();

    san_f = City(name="San Francisco", state=State(name="California"))

    session.add(san_f);
    session.commit();
