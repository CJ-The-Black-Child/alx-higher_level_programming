#!/usr/bin/python3
"""
Prints the first state object from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":

    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost/{}".format(
                sys.argv[1], sys.argv[2], sys.argv[3]
                ), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    first_state = session.query(State).order_by(State.id).first()
    if first_state is None:
        print("Nothing")
    else:
        print("{}: {}".format(first_state.id, first_state.name))

    session.close()
