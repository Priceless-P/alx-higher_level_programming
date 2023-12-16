#!/usr/bin/python3
"""
Changes the name of a State object in the database
"""

import sys
import sqlalchemy
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def insert_states():
    """Changes state obj"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    new_state = session.query(State).get(2)
    new_state.name = "New Mexico"
    session.commit()
    session.close()


if __name__ == '__main__':
    insert_states()
