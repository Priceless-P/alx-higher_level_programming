#!/usr/bin/python3
"""
Deletes the State objects that contains 'a' in the database
"""

import sys
import sqlalchemy
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def delete_states():
    """Deletes state obj"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).filter(State.name.like("%a%"))
    for state in states:
        session.delete(state)
    session.commit()
    session.close()


if __name__ == '__main__':
    delete_states()
