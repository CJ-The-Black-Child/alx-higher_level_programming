#!/usr/bin/python3
"""
Changes the name of the State object where id=2 to New Mexico from a
database
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                username, password, database)
            )
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states_with_a = session.query(State).filter(State.name.like('%a%')).all()

    for state in states_with_a:
        session.delete(state)

    session.commit()
    session.close()
