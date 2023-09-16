#!/usr/bin/python3
"""a python file that contains the class definition of a State """
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String


Base = declarative_base()


class State(Base):
    """Class definition for states"""

    __tablename__ = "states"
    id = Column(
        Integer, primary_key=True, autoincrement=True,
        nullable=False, unique=True
    )
    name = Column(String(128), nullable=False)
