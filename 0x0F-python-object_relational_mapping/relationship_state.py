#!/usr/bin/python3
"""a  python file that contains the class definition of a State
and an instance Base = declarative_base()"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


Base = declarative_base()


class State(Base):
    """class definition for the state class"""

    __tablename__ = "states"
    id = Column(
        Integer, primary_key=True, autoincrement=True, nullable=False,
        unique=True
    )
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state",
                          cascade="all, delete-orphan")
