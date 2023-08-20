#!/usr/bin/python3
"""
Changes the name of the State object with id = 2 to
New Mexico in the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                username, password, database), pool_pre_ping=True
            )

    Session = sessionmaker(bind=engine)
    session = Session()

    state_id_to_update = 2
    new_name = "New Mexico"

    state = session.query(State).filter_by(id=state_id_to_update).first()

    if state:
        state.name = new_name
        session.commit()
        print(f"State with id {state.id} updated to '{new_name}'")
    else:
        print(f"State with id {state_id_to_update} not found")

    session.close()
