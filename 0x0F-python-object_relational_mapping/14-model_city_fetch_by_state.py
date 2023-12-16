#!/usr/bin/python3
"""
Prints all cities by state id from the database
"""

import sys
import sqlalchemy
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def get_cities():
    """Gets cities"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    all = session.query(State, City).order_by(City.id).filter(
            City.state_id == State.id)

    for state, city in all:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()


if __name__ == '__main__':
    get_cities()
