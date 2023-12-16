#!/usr/bin/python3
"""
Prints all states from the database
"""

import sys
import sqlalchemy
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def get_states():
    """Gets states"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = None
    states = session.query(State).filter(
                State.name.like(sys.argv[4]))

    for state in states:
        print("{}".format(state.id))
    if (not state):
        print("Not found")
    session.close()


if __name__ == '__main__':
    get_states()
