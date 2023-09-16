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

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    cali_state = State(name="California")
    sans_city = City(name="San Francisco", state_id=cali_state.id)
    cali_state.cities.append(sans_city)

    session.add_all([cali_state, sans_city])
    session.commit()
    session.close()
