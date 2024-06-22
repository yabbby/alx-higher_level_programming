#!/usr/bin/python3
"""Database"""

import sys

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    cur_session = Session()
    obj = cur_session.query(State).first()
    if not obj:
        print("Nothing")
    else:
        print(f'{obj.id}: {obj.name}')
