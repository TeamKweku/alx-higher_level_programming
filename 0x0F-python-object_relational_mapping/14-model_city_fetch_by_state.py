#!/usr/bin/python3
"""Script that prints all City objects from the database"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

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

    cities_states = (
        session.query(City, State)
        .order_by(City.id)
        .join(State, City.state_id == State.id)
        .all()
    )

    for city, state in cities_states:
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()
