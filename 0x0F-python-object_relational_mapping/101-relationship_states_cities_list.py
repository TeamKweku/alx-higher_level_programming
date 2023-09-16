#!/usr/bin/python3
"""
Script that creates the State "California" with the City "San Francisco"
from the database hbtn_0e_100_usa
"""
import sys
from sqlalchemy import create_engine
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} <username> <passwd> <database>")
        sys.exit(1)

    username, passwd, database = sys.argv[1], sys.argv[2], sys.argv[3]
    engine = create_engine(
        f"mysql+mysqldb://{username}:{passwd}@localhost/{database}",
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    result = (
        session.query(State, City)
        .filter(State.id == City.state_id)
        .order_by(State.id, City.id).all()
    )

    curr_state_id = None

    for state, city in result:
        if state.id != curr_state_id:
            print(f"{state.id}: {state.name}")
            curr_state_id = state.id
        print(f"\t{city.id}: {city.name}")

    session.close()
