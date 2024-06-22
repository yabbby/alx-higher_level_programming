#!/usr/bin/python3
"""Database"""

import sys

from model_city import City
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    cur_session = Session()
    for city, state in cur_session.query(City, State).join(State):
        print(f"{state.name}: ({city.id}) {city.name}")
