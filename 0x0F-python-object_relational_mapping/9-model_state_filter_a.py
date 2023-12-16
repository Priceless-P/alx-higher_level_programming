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
    states = session.query(State).order_by(State.id).filter(
                State.name.like("%a%"))

    for state in states:
        print("{}:{}".format(state.id, state.name))
    session.close()


if __name__ == '__main__':
    get_states()
