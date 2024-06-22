#!/usr/bin/python3
"""Database"""

import sys

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    state_name = sys.argv[4]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    cur_session = Session()
    res = cur_session.query(State).filter_by(name=state_name).all()
    if res:
        for row in res:
            print(row.id)
    else:
        print("Not found")
