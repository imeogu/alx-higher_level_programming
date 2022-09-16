#!/usr/bin/python3
''' Lists all City objects from the database hbtn_0e_101_usa
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
    #engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]));
    engine = create_engine('mysql+mysqldb://root:Lilstex4good95@localhost:3306/hbtn_0e_101_usa', pool_pre_ping=True);
    
    Session = sessionmaker(bind=engine);
    session = Session();

    cities = session.query(City).order_by(City.id)
    for city in cities:
        print('{}: {} -> {}'.format(city.id, city.name, city.state.name))
    